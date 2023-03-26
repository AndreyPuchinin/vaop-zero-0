# ЗАДАЧА: Объединить Бизнес, Программиста и Машину

# В списке много ячеек (агентов)

# В одной ячейке:
# поле Бизнес - business
# поле Программист - programmer
# поле Машина - machine
# поле текущий шаг - current id
# поле переход (след. шаг) - next id

from pprint import pprint

"""дописать вывод самих агентов при вызове exception"""
class InfinityCyclingError(Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        print('Error: infinity cycling!')
        if self.message:
            return f'Cycle: {self.message}'
        else:
            return 'MyCustomError has been raised'


class Runner:
    def __init__(self, agents: list) -> None:
        self.agents = agents

    def show_business(self) -> list:
        return [f'{one_agent.show_business()}' for one_agent in self.agents]

    def show_programmer(self) -> list:
        return [f'{one_agent.show_programmer()}' for one_agent in self.agents]

    def show_machine(self) -> list:
        return [f'{one_agent.show_machine()}' for one_agent in self.agents]

    def show_all(self) -> tuple:
        return self.show_business(), self.show_programmer(), self.show_machine()

    def find_agent(self, cur_agent_id: int):
        for one_agent in self.agents:
            if one_agent.cur_id == cur_agent_id:
                return one_agent
        return None

    def run(self) -> None:
        """Перемещается по агентам согласно их кодам-ссылкам не следующего
        Также имеет проверку на бескоенчные циклы
        Бесконечный цикл выписывается исключительно от его начала до конца
        Например:
        100->200->300->400->200
        выпишет
        200->300->400->200
        и остановит выполеннение на 400"""
        first_agent = self.agents[0]
        agents_ids = [first_agent.cur_id]
        first_agent.run()
        next_agent = self.find_agent(first_agent.next_id)
        while next_agent is not None:
            next_agent.run()
            if next_agent.cur_id not in agents_ids:
                agents_ids.append(next_agent.cur_id)
            else:
                agents_ids.append(next_agent.cur_id)
                raise InfinityCyclingError(agents_ids[agents_ids.index(next_agent.cur_id):])
            next_agent = self.find_agent(next_agent.next_id)


class Agent:
    def __init__(self, *args) -> None:
        self.business, self.programmer, self.machine, \
        self.cur_id, self.next_id = args

    def show_business(self) -> str:
        return f'{self.cur_id}->{self.next_id}. {self.business}'

    def show_programmer(self) -> str:
        return f'{self.cur_id}->{self.next_id}. {self.programmer}'

    def show_machine(self) -> str:
        return f'{self.cur_id}->{self.next_id}. {self.machine}'

    def show_all(self) -> tuple:
        return self.show_business(), self.show_programmer(), self.show_machine()

    def run(self) -> str:
        pprint(self.show_all())
        return self.machine()


def test1() -> None:
    print('test1')


def test2() -> None:
    print('test2')


if __name__ == '__main__':
    agent1 = Agent('БИЗНЕС: протесировать 1', 'ПРОГРАММИСТ: test1',
                   test1, 100, 200)
    agent2 = Agent('БИЗНЕС: протесировать 2', 'ПРОГРАММИСТ: test2',
                   test1, 200, 300)
    agent3 = Agent('БИЗНЕС: создать агента 3', 'agent3 = Agent(...)',
                   lambda: None, 300, 400)
    agent4 = Agent('БИЗНЕС: создать агента 4', 'agent4 = Agent(...)',
                   lambda: None, 400, 200)
    runner = Runner([agent1, agent2, agent3,
                     agent4])
    pprint(f'{runner.show_all()=}')
    runner.run()