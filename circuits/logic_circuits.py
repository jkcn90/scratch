from logic_gates import LogicGate, BinaryGate, NotGate, AndGate, OrGate, XorGate
from logic_gate_pins import InputPin, OutputPin, create_pin_closure

class AdderCircuit(BinaryGate):

    def __init__(self, name, verbose=False):
        BinaryGate.__init__(self, name, verbose)
        self.carry_in_pin = InputPin(self, 'carry in', verbose)
        self.carry_out_pin = OutputPin(self, 'carry out', verbose)

    carry_in = create_pin_closure('carry_in_pin')
    carry_out = create_pin_closure('carry_out_pin')

    def update(self):
        return

    def get_output(self):
        value = self.output_pin.value
        value = int(value) if value is not None else None
        return value

    def get_carry_out(self):
        value = self.carry_out_pin.value
        value = int(value) if value is not None else None
        return value

class HalfAdder(AdderCircuit):

    def __init__(self, name, verbose=False):
        AdderCircuit.__init__(self, name, verbose)
        del self.carry_in

        verbose = True if verbose > 1 else False
        gate_name = '{} (Half Adder'.format(name) + ' Internal {})'

        xor_gate = XorGate(gate_name.format('XOR Gate'), verbose)
        and_gate = AndGate(gate_name.format('AND Gate'), verbose)

        and_gate.input_1 = self.input_1
        xor_gate.input_1 = self.input_1

        and_gate.input_2 = self.input_2
        xor_gate.input_2 = self.input_2

        self.output = xor_gate.output
        self.carry_out = and_gate.output

class FullAdder(AdderCircuit):

    def __init__(self, name, verbose=False):
        AdderCircuit.__init__(self, name, verbose)

        verbose = True if verbose > 1 else False
        gate_name = '{} (Full Adder'.format(name) + ' Internal {})'

        half_adder_1 = HalfAdder(gate_name.format('Half Adder 1'), verbose)
        half_adder_2 = HalfAdder(gate_name.format('Half Adder 2'), verbose)
        or_gate = OrGate(gate_name.format('OR Gate'), verbose)

        half_adder_1.input_1 = self.input_1
        half_adder_1.input_2 = self.input_2

        half_adder_2.input_1 = self.carry_in
        half_adder_2.input_2 = half_adder_1.output
        
        or_gate.input_1 = half_adder_2.carry_out
        or_gate.input_2 = half_adder_1.carry_out

        self.output = half_adder_2.output
        self.carry_out = or_gate.output

def add_binary_strings(first_binary_string, second_binary_string, verbose):
    previous_full_adder = None

    output = []
    for i, (x, y), in enumerate(zip(reversed(first_binary_string),
                               reversed(second_binary_string))):

        full_adder = FullAdder('2 ^ {} place'.format(i), verbose)

        if verbose:
            print('\nProcessing {}'.format(full_adder.name))

        if previous_full_adder is None:
            full_adder.carry_in = 0
        else:
            full_adder.carry_in = previous_full_adder.carry_out

        full_adder.input_1 = int(x)
        full_adder.input_2 = int(y)

        previous_full_adder = full_adder
        output.append(full_adder)

    carry = full_adder.get_carry_out()

    output = list(reversed([full_adder.get_output() for full_adder in output]))
    output = [carry] + output if carry == 1 else output
    return ''.join([str(x) for x in output])

if __name__ == '__main__':
    verbose = 1
    # Test Logic Circuits
    print('--------------------------Half Adder----------------------')
    half_adder = HalfAdder('Test Half Adder', verbose=verbose)
    half_adder.input_1 = 1
    half_adder.input_2 = 1
    msg = 'output: {} carry_out: {}'
    msg = msg.format(half_adder.get_output(), half_adder.get_carry_out())
    print(msg)
    print()
    half_adder = HalfAdder('Test Half Adder', verbose=verbose)
    half_adder.input_1 = 1
    half_adder.input_2 = 0
    msg = 'output: {} carry_out: {}'
    msg = msg.format(half_adder.get_output(), half_adder.get_carry_out())
    print(msg)
    print()
    half_adder = HalfAdder('Test Half Adder', verbose=verbose)
    half_adder.input_1 = 0
    half_adder.input_2 = 1
    msg = 'output: {} carry_out: {}'
    msg = msg.format(half_adder.get_output(), half_adder.get_carry_out())
    print(msg)
    print()
    half_adder = HalfAdder('Test Half Adder', verbose=verbose)
    half_adder.input_1 = 0
    half_adder.input_2 = 0
    msg = 'output: {} carry_out: {}'
    msg = msg.format(half_adder.get_output(), half_adder.get_carry_out())
    print(msg)
    print()

    verbose = 1
    print('--------------------------Full Adder----------------------')
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 1
    full_adder.input_1 = 1
    full_adder.input_2 = 1
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 0
    full_adder.input_1 = 1
    full_adder.input_2 = 1
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 1
    full_adder.input_1 = 1
    full_adder.input_2 = 0
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 0
    full_adder.input_1 = 1
    full_adder.input_2 = 0
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 1
    full_adder.input_1 = 0
    full_adder.input_2 = 1
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 0
    full_adder.input_1 = 0
    full_adder.input_2 = 1
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 1
    full_adder.input_1 = 0
    full_adder.input_2 = 0
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()
    full_adder = FullAdder('Test Full Adder', verbose=verbose)
    full_adder.carry_in = 0
    full_adder.input_1 = 0
    full_adder.input_2 = 0
    msg = 'output: {} carry_out: {}'
    msg = msg.format(full_adder.get_output(), full_adder.get_carry_out())
    print(msg)
    print()

    print('--------------------------Four Bit Addition-------------------')
    verbose = 1
    first_binary_string = '0100'
    second_binary_string = '0010'
    output = add_binary_strings(first_binary_string, second_binary_string,
                                verbose)
    print()
    print('first binary string: {}'.format(first_binary_string))
    print('second binary string: {}'.format(second_binary_string))
    print('sum: {}'.format(output))
