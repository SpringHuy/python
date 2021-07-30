import iso6346

class Shipping1:
    """
        With more about static methods
    """
    _next_serial = 1
    
    def _generate_serial(self):
        result = Shipping1._next_serial
        Shipping1._next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._serial = self._generate_serial()



class ShippingContainer:

    _next_serial = 1000

    @staticmethod
    def _generate_serial():
        """
            Associate the method with the class instead of the instance: 
            1. use static method
            2. Call the method via the class name
        """
        result = ShippingContainer._next_serial
        ShippingContainer._next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def _gen_serial(cls):
        result = cls._next_serial
        cls._next_serial += 1
        return result
    
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, _contents = [])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, _contents=list(items))

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        #self._bic = ShippingContainer._make_bic_code(
        self._bic = self._make_bic_code(        #ensure polymophism when calling the static methods from child class
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

        self._serial = ShippingContainer._gen_serial()        
        #self._serial = ShippingContainer._next_serial
        #ShippingContainer._next_serial += 1
        ##self._next_serial -> create instance attribute that mask the class variable


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )

def main():
    c1 = ShippingContainer("A", "A")
    c2 = ShippingContainer("B", "B")
    c3 = ShippingContainer("C", "C")
    print(c1._serial, c2._serial, c3._serial)
    print(ShippingContainer._next_serial)

## += read,write, modify
if __name__ == '__main__':
    main()


