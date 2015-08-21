class Pin:
    def __init__(self, circuit, name, is_input_pin=False, verbose=False):
        self._value = None

        self.connected_pins = []

        self.name = name
        self.circuit = circuit
        self.is_input_pin = is_input_pin

        self.verbose = verbose

    def connect(self, inputs):
        if type(inputs) != list:
            inputs = [inputs]
        for input in inputs:
            self.connected_pins.append(input)
        self.circuit.update()

    def clear_connections(self):
        self.connected_pins = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._value == value:
            return

        self._value = value

        if self.verbose:
            msg = '"{}" <{}> set to {}'
            msg = msg.format(self.circuit.name, self.name, self._value)
            print(msg)

        if self.is_input_pin:
            self.circuit.update()

        for pin in self.connected_pins:
            pin.value = value

    def __str__(self):
        msg = '"{}" <{}>'
        msg = msg.format(self.circuit.name, self.name, self.value)
        return msg

    def __repr__(self):
        msg = '"{}" <{}> with value: {}'
        msg = msg.format(self.circuit.name, self.name, self.value)
        return msg

class InputPin(Pin):

    def __init__(self, circuit, name, verbose=False):
        Pin.__init__(self, circuit, name, is_input_pin=True, verbose=verbose)

class OutputPin(Pin):

    def __init__(self, circuit, name, verbose=False):
        Pin.__init__(self, circuit, name, is_input_pin=False, verbose=verbose)

def create_pin_closure(pin):

    def get_pin(self):
        self_pin = getattr(self, pin)
        return self_pin

    def set_pin(self, value):
        self_pin = getattr(self, pin)
        if isinstance(value, Pin):
            value.connect(self_pin)
            self_pin.value = value.value
        else:
            self_pin.value = value

    def del_pin(self):
        self_pin = getattr(self, pin)
        del self_pin

    return property(get_pin, set_pin, del_pin, 'test')
