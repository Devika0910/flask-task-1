from flask import Flask
fact = Flask(__name__)




@fact.route('/<int:num>')
def abc(num):
    if num==0:
        return '1'
    elif num>0:
        factt=1
        for i in range(1,num+1):
            factt=factt*i
        return f'{factt}'
    else:
        return "no factorial"   
        
if __name__ == '__main__':
    fact.run(debug=True)        