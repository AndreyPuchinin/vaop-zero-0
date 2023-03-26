from system_runner import *
from vaop_zero_agents import *

if __name__ == '__main__':
    glob_vars = []
    create_parser = Agent('создаем парсер',
                          'создаем класс и объект',
                          create_parser, 100, 200)
    runner = Runner([create_parser])
    runner.run()