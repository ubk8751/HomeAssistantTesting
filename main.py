import os
import yaml
import asyncio
from unittest.mock import AsyncMock
from homeassistant import core
from homeassistant.setup import async_setup_component
from utils.get_kwargs import get_kwargs
from utils.Error import InvalidFileExtension
from utils.HASScript import HASScript

EVENT_TAG_SCANNED = "tag_scanned"


async def test_scrip(script:dict, debug:bool):
    """
    Test the tag toggle alarm automation.
    
    :param dict script: The script to be tested. Should be of type dictionary,
    read using the get_script() function.
    """
    # Create a Home Assistant instance
    hass = core.HomeAssistant()
    
    hass.config.config_dir = "/tmp/test_config"
    os.makedirs(hass.config.config_dir, exist_ok=True)

    # Create a minimal configuration.yaml
    config_file = os.path.join(hass.config.config_dir, "configuration.yaml")
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            f.write("homeassistant:\n")

    # Set up mock states
    alarm_entity = "alarm_control_panel.alarmo"
    hass.states.async_set(alarm_entity, "disarmed")  # Initial state of the alarm

     # Load the automation
    assert await async_setup_component(hass, "homeassistant", {})
    assert await async_setup_component(hass, "automation", {"automation": [script]})

    # Register mock services for arming and disarming
    arm_away_mock = AsyncMock()
    disarm_mock = AsyncMock()
    hass.services.async_register(
        "alarm_control_panel", "alarm_arm_away", arm_away_mock
    )
    hass.services.async_register(
        "alarm_control_panel", "alarm_disarm", disarm_mock
    )

    # Simulate a tag scan event
    hass.bus.async_fire(
        EVENT_TAG_SCANNED, {"tag_id": "04-B4-95-5A-B4-6D-80", "device_id": "some_device"}
    )
    await hass.async_block_till_done()

    # Validate the alarm was armed
    assert arm_away_mock.call_count == 1
    assert disarm_mock.call_count == 0

    # Change the alarm state to armed
    hass.states.async_set(alarm_entity, "armed_away")

    # Simulate another tag scan
    hass.bus.async_fire(
        EVENT_TAG_SCANNED, {"tag_id": "04-B4-95-5A-B4-6D-80", "device_id": "some_device"}
    )
    await hass.async_block_till_done()

    # Validate the alarm was disarmed
    assert disarm_mock.call_count == 1
    assert arm_away_mock.call_count == 1

    # Clean up
    await hass.async_stop()

if __name__ == '__main__':
    args = get_kwargs()
    try:
        if '.hasscript' not in args.script_name:
            raise InvalidFileExtension
        script_path = os.path.join(os.getcwd(), 'scripts', args.script_name)
    except InvalidFileExtension as e:
        print(f"Error: {e}")
        raise
    script_obj =  HASScript(name=args.script_name)
    script_obj.init_script(script_path=script_path)
    asyncio.run(test_scrip(script=script_obj.script, debug=args.debug))