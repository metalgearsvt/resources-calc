import programFlow.MainPrompt as MP

session = MP.MainPrompt()

print(session.get_test())
session.set_test("NEW VAL")
print(session.get_test())
