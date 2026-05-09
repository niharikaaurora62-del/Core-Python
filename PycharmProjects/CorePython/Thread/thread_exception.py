from threading import Thread
class Hi(Thread):
    def run(self):
        try:
            print('Hi')
            result = 10/0
            print("Result",result)
        except Exception as e:
            print(e)
t = Hi()
t.start()
