class PaymentMethodsNotAvailableException(Exception):
    def __init__(self):
        self.message = 'This payment method is not available'
        super().__init__(self.message)


class PaymentMethodDiscountAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Already exists a discount with this payment method'
        super().__init__(self.message)

class CouponCodeAleradyExistsException(Exception):
    def __init__(self):
        self.message = 'coupoun already exists'
        super().__init__(self.massage)

class AdminEmailAlreadyExists(Exception):
    def __init__(self):
        self.message = 'this admin email already exists'
        super().__init__(self.massage)


    