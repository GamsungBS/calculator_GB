import sys
from PyQt5.QtWidgets import *
import numpy as np

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_Grid = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.equation_solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(self.equation_solution)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_remainder = QPushButton("%")
        
        ### 역수 제곱 제곱근 버튼 생성
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_squareRoot = QPushButton("2√x")
        
        ### 사칙연산+(%) 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))

        ### 역수 제곱 제곱근 버틑 클릭시 시그널 설정
        button_reciprocal.clicked.connect(lambda state, operation = "1/": self.button_reciprocal_clicked(operation))
        button_squareRoot.clicked.connect(lambda state, operation = "**0.5": self.button_squareRoot_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "**2": self.button_squared_clicked(operation))
        
        ### 사칙연산+(%) 버튼을 layout_Grid 레이아웃에 추가
        layout_Grid.addWidget(button_plus, 4, 3)
        layout_Grid.addWidget(button_minus, 3, 3)
        layout_Grid.addWidget(button_product, 2, 3)
        layout_Grid.addWidget(button_division, 1, 3)
        layout_Grid.addWidget(button_remainder, 0, 0)
        
        ### 역수 제곱 제곱근 버튼 layout에 추가
        layout_Grid.addWidget(button_reciprocal, 1, 0)
        layout_Grid.addWidget(button_square, 1, 1)
        layout_Grid.addWidget(button_squareRoot, 1, 2)

        ### =, C, CE, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_C = QPushButton("C")
        button_CE = QPushButton("CE")
        button_backspace = QPushButton("Backspace")
    

        ### =, C, CE, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_C.clicked.connect(self.button_clear_clicked)
        button_CE.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, C, CE, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_Grid.addWidget(button_C, 0, 2)
        layout_Grid.addWidget(button_CE, 0, 1)
        layout_Grid.addWidget(button_backspace, 0, 3)
        layout_Grid.addWidget(button_equal, 5, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number+5, 3)
                layout_Grid.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_Grid.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_Grid.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_Grid.addWidget(button_double_zero, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_Grid)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    
    def add_to_expression(self, value):
        self.equation_solution += str(value)
    
    def number_button_clicked(self, num):
        equation_solution = self.equation_solution.text()
        equation_solution += str(num)
        self.equation_solution.setText(equation_solution)

    def button_operation_clicked(self, operation):
        equation_solution = self.equation_solution.text()
        equation_solution += operation
        self.equation_solution.setText(equation_solution)
        
    def button_reciprocal_clicked(self, operation):
        equation_solution = operation
        equation_solution += self.equation_solution.text()
        self.equation_solution.setText(equation_solution)
        equation_solution = eval(equation_solution)
        self.equation_solution.setText(str(equation_solution))

        
    def button_squared_clicked(self, operation):
        equation_solution = self.equation_solution.text()
        equation_solution += operation
        self.equation_solution.setText(equation_solution)
        equation_solution = self.equation_solution.text()
        equation_solution = eval(equation_solution)
        self.equation_solution.setText(str(equation_solution))

    def button_squareRoot_clicked(self, operation):
        equation_solution = self.equation_solution.text()
        equation_solution += operation
        self.equation_solution.setText(equation_solution)
        equation_solution = self.equation_solution.text()
        equation_solution = eval(equation_solution)
        self.equation_solution.setText(str(equation_solution))

    def button_equal_clicked(self):
        equation_solution = self.equation_solution.text()
        equation_solution = eval(equation_solution)
        self.equation_solution.setText(str(equation_solution))
        
    def button_clear_clicked(self):
        self.equation_solution.setText("")
        self.equation_solution.setText("")

    def button_backspace_clicked(self):
        equation_solution = self.equation_solution.text()
        equation_solution = equation_solution[:-1]
        self.equation_solution.setText(equation_solution)


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
