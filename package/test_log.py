from logfile import Logclass

class TestExample(Logclass):
    def test_logs(self):
        log = self.get_the_log()
        log.info("This is test case")
        log.info("test case started")

        if 'car' in 'newcardrive':
            assert True
            log.info("test case pass")
        else:
            assert False
            log.error("test case failed")