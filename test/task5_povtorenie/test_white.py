import pytest
from user_validator import UserValidator

class Test:
    def s(self):
        self.v = UserValidator()
        
    def t(self):
        assert self.v._strong("Abc123") == True
        assert self.v._strong("abc") == False
        assert self.v._strong("ABCDEF") == True
        assert self.v._strong("abc123") == False
        
    def te(self):
        assert self.v.validate("", "Abc123", 25) == {"ok": False, "msg": "No username"}
