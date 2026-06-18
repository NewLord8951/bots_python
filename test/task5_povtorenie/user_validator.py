class UserValidator:
    def __init__(self):
        self._failed = {}
        self._blocked = set()
    
    def _strong(self, pwd):
        return len(pwd) >= 6 and any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd)
    
    def validate(self, username, password, age):
        if not username:
            return {"ok": False, "msg": "No username"}
        if not (18 <= age <= 99):
            return {"ok": False, "msg": "Bad age"}
        if username in self._blocked:
            return {"ok": False, "msg": "Blocked"}
        if not self._strong(password):
            self._failed[username] = self._failed.get(username, 0) + 1
            if self._failed[username] >= 3:
                self._blocked.add(username)
            return {"ok": False, "msg": "Weak password"}
        return {"ok": True, "msg": "OK"}