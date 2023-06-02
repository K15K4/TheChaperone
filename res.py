label_name = QLabel('<font size="4"> Логин </font>')
self.login_edit = QtWidgets.QLineEdit()
self.login_edit.setPlaceholderText('Пожалуйста введите ваш логин')
layout.addWidget(label_name, 0, 0)
layout.addWidget(self.login_edit, 0, 1)

label_password = QLabel('<font size="4"> Пароль </font>')
self.lineEdit_password = QLineEdit()
self.password_edit.setPlaceholderText('Пожалуйста введите ваш пароль')
self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
layout.addWidget(label_password, 1, 0)
layout.addWidget(self.password_edit, 1, 1)

login_button = QPushButton('Войти')
self.login_button.clicked.connect(self.on_login)
layout.addWidget(login_button, 2, 0, 1, 2)
layout.setRowMinimumHeight(2, 75)

self.setLayout(layout)
