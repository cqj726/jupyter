import sys
class MyErr(Exception):
    def __str__(self):
        return "I'm a self-defined Error!"
def main():
    try:
        if len(sys.argv)==1:
            raise MyErr()
    except MyErr as e:
        print(e)
        
main()