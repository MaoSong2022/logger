

import logger
import example_module

# you can change the name of debug file
log = logger.setup_applevel_logger(file_name="app_debug.log")


def main():
    a, b = 2, 3
    c = example_module.example_function(2, 3)
    print(c)


if __name__ == '__main__':
    main()