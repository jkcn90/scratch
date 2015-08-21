import inspect
from logic_gate_pins import InputPin, OutputPin , create_pin_closure

class LogicGate():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class UnaryGate(LogicGate):

    def __init__(self, name, verbose=False):
        LogicGate.__init__(self, name)

        self.input_pin = InputPin(self, 'input', verbose)
        self.output_pin = OutputPin(self, 'output', verbose)

    input = create_pin_closure('input_pin')
    output = create_pin_closure('output_pin')

    def set_verbose(self, verbose=True):
        self.input.verbose = verbose
        self.output_pin.verbose = verbose

    def update(self):
        if self.input_pin.value is None:
            value = None
        else:
            value = self.execute_gate_logic() 
        self.output = value

class BinaryGate(LogicGate):

    def __init__(self, name, verbose=False):
        LogicGate.__init__(self, name)

        self.input_1_pin = InputPin(self, 'input 1', verbose)
        self.input_2_pin = InputPin(self, 'input 2', verbose)
        self.output_pin = OutputPin(self, 'output', verbose)

    input_1 = create_pin_closure('input_1_pin')
    input_2 = create_pin_closure('input_2_pin')
    output = create_pin_closure('output_pin')

    def set_verbose(self, verbose=True):
        self.input_1_pin.verbose = verbose
        self.input_2_pin.verbose = verbose
        self.output_pin.verbose = verbose

    def update(self):
        if self.input_1_pin.value is None or self.input_2_pin.value is None:
            value = None
        else:
            value = self.execute_gate_logic() 
        self.output = value
        
class NotGate(UnaryGate):

    def __init__(self, name, verbose=False):
        UnaryGate.__init__(self, name, verbose)

    def execute_gate_logic(self):
        return not self.input.value

class AndGate(BinaryGate):

    def __init__(self, name, verbose=False):
        BinaryGate.__init__(self, name, verbose)

    def execute_gate_logic(self):
        return self.input_1.value and self.input_2.value

class OrGate(BinaryGate):

    def __init__(self, name, verbose=False):
        BinaryGate.__init__(self, name, verbose)

    def execute_gate_logic(self):
        return self.input_1.value or self.input_2.value

class XorGate(BinaryGate):

    def __init__(self, name, verbose=False):
        BinaryGate.__init__(self, name, verbose)

        verbose = True if verbose > 1 else False
        
        gate_name = '{} (XOR'.format(name) + ' Internal {})'

        or_gate = OrGate(gate_name.format('OR Gate'), verbose)
        and_gate_1 = AndGate(gate_name.format('AND Gate 1'), verbose)
        and_gate_2 = AndGate(gate_name.format('AND Gate 2'), verbose)
        not_gate_1 = NotGate(gate_name.format('NOT Gate 1'), verbose)
        not_gate_2 = NotGate(gate_name.format('NOT Gate 2'), verbose)

        and_gate_1.input_1 = self.input_1
        not_gate_2.input = self.input_1

        and_gate_2.input_1 = self.input_2
        not_gate_1.input = self.input_2

        and_gate_1.input_2 = not_gate_1.output
        and_gate_2.input_2 = not_gate_2.output

        or_gate.input_1 = and_gate_1.output
        or_gate.input_2 = and_gate_2.output
        self.output = or_gate.output

    def execute_gate_logic(self):
        return self.output.value

if __name__ == '__main__':
    verbose = 1
    # Test Basic Logic Gates
    print('--------------------------NOT--------------------------')
    not_gate = NotGate('Test NOT Gate', verbose=verbose)
    not_gate.input = True
    print()
    not_gate.input = False
    print()

    print('--------------------------AND--------------------------')
    and_gate = AndGate('Test AND Gate', verbose=verbose)
    and_gate.input_1 = True
    and_gate.input_2 = True
    print()
    and_gate = AndGate('Test AND Gate', verbose=verbose)
    and_gate.input_1 = True
    and_gate.input_2 = False
    print()
    and_gate = AndGate('Test AND Gate', verbose=verbose)
    and_gate.input_1 = False
    and_gate.input_2 = True
    print()
    and_gate = AndGate('Test AND Gate', verbose=verbose)
    and_gate.input_1 = False
    and_gate.input_2 = False
    print()

    print('--------------------------Or---------------------------')
    or_gate = AndGate('Test OR Gate', verbose=verbose)
    or_gate.input_1 = True
    or_gate.input_2 = True
    print()
    or_gate = AndGate('Test OR Gate', verbose=verbose)
    or_gate.input_1 = True
    or_gate.input_2 = False
    print()
    or_gate = AndGate('Test OR Gate', verbose=verbose)
    or_gate.input_1 = False
    or_gate.input_2 = True
    print()
    or_gate = AndGate('Test OR Gate', verbose=verbose)
    or_gate.input_1 = False
    or_gate.input_2 = False
    print()

    # Test Composite Circuits
    print('--------------------------XOR--------------------------')
    xor_gate = XorGate('Test XOR Gate', verbose=verbose)
    xor_gate.input_1 = True
    xor_gate.input_2 = True
    print()
    xor_gate = XorGate('Test XOR Gate', verbose=verbose)
    xor_gate.input_1 = True
    xor_gate.input_2 = False
    print()
    xor_gate = XorGate('Test XOR Gate', verbose=verbose)
    xor_gate.input_1 = False
    xor_gate.input_2 = True
    print()
    xor_gate = XorGate('Test XOR Gate', verbose=verbose)
    xor_gate.input_1 = False
    xor_gate.input_2 = False
    print()
