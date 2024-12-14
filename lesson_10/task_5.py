class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        if len(self) % len(s) != 0:
            return False
        return self == s * (len(self) // len(s))

    def is_palindrom(self):
        normalized_str = self.lower()
        return normalized_str == normalized_str[::-1]


s = SuperStr("abab")
print(s.is_repeatance("ab"))
print(s.is_repeatance("abc"))

s2 = SuperStr("level")
print(s2.is_palindrom())

s3 = SuperStr("Hello")
print(s3.is_palindrom())

s4 = SuperStr("")
print(s4.is_palindrom())
