class Logic:
    def __init__(self):
        self._current_value = 0.0
        self._last_value = 0.0
        self._last_operation = _no_operation
        self._ready_for_new_input = True
        self._current_display = "0"

    def display(self) -> str:
        '''
        Changes the string which is how
        the app is based on in (str)
        '''
        return self._current_display
    
    def _format_display(self, value: float) -> str:
        '''
        Format a float value for display, removing unnecessary .0
        '''
        if value == int(value):
            return str(int(value))
        else:
            return str(value)
    
    def commence(self, key: str) -> None:
        '''
        Calls the function that correlates to
        whichever key was selected.
        '''
        if key.isdigit():
            # If ready for new input, clear the current value first
            if self._ready_for_new_input:
                self._current_value = 0.0
                self._current_display = "0"
                self._ready_for_new_input = False
            
            # Add digit to display string
            if self._current_display == "0":
                self._current_display = key
            else:
                self._current_display += key
            
            # Update the actual value for calculations
            self._current_value = float(self._current_display)
        elif key == '.':
            # Only add decimal point if there isn't already one
            if '.' not in self._current_display:
                self._current_display += '.'
                self._current_value = float(self._current_display)
        elif key == '%':
            if self._last_value != 0:
                result = self._last_operation(self._last_value, self._current_value)
                self._current_value = result
            else:
                # If no previous operation, calculate percentage of current value
                self._current_value = self._current_value / 100.0
            # Update display
            self._current_display = self._format_display(self._current_value)
            self._ready_for_new_input = True
        elif key == '+/-':
            # Negate the current value
            self._current_value = -self._current_value
            self._current_display = self._format_display(self._current_value)
        elif key in ['=', '+', '-', '*', '/']:
            result = self._last_operation(self._last_value, self._current_value)

            if key == '=':
                self._last_value = 0
                self._current_value = result
                self._current_display = self._format_display(self._current_value)
                self._ready_for_new_input = True
            else:
                self._last_value = result
                self._current_value = result  # Show the result instead of 0
                self._current_display = self._format_display(self._current_value)
                self._ready_for_new_input = True

            if key == '+':
                self._last_operation = _add_operation
            elif key == '-':
                self._last_operation = _subtract_operation
            elif key == '*':
                self._last_operation = _multiply_operation
            elif key == '/':
                self._last_operation = _divide_operation
            else:
                self._last_operation = _no_operation


def _no_operation(stored: float, current: float) -> float:
    '''
    used when no operation is in queue;
    returning the current value.
    '''
    return current

def _add_operation(stored: float, current: float) -> float:
    '''
    used when 'add' is selected as the
    operation to use;
    returns the new value.
    '''
    return stored + current

def _subtract_operation(stored: float, current: float) -> float:
    '''
    used when 'subtract' is selected as the
    operation to use;
    returns the new value.
    '''
    return stored - current

def _multiply_operation(stored: float, current: float) -> float:
    '''
    used when 'multiply' is selected as the
    operation to use;
    returns the new value.
    '''
    return stored * current

def _divide_operation(stored: float, current: float) -> float:
    '''
    used when 'divide' is selected as the
    operation to use;
    returns the new value.
    '''
    if current == 0:
        return 0.0
    return stored / current