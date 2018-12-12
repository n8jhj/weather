def pytest_sessionstart(session):
    print(session)

def pytest_sessionfinish(session, exitstatus):
    print(exitstatus)
