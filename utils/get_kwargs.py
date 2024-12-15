import argparse

def get_kwargs() -> argparse.Namespace:
    # InItiate the parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument('--script',
                        type=str,
                        dest='script_name',
                        required=True,
                        help='The name of the script to test.')
    parser.add_argument('--script-name',
                        type=str,
                        dest='script_name',
                        default='test_scrip',
                        help='Optional argument to set a name to your script in-code.')
    parser.add_argument('--debug',
                        action='store_true',
                        help='Toggles debugging prints.')

    # Parse arguments
    args = parser.parse_args()
    
    return args    