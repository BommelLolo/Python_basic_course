class A:  # equal to `class A(object):`
    def method(self):
        print('called in class A')


class B(A):
    pass


class B1:
    def method(self):
        print('called in class B1')
        super().method()

    def unique_method(self):
        print('called unique in class B1')


class C(A):
    def method(self):
        print('called in class C')


class D(C):
    def method(self):
        print('called in class D')
        super().method()


class E(B):
    def method(self):
        print('called in class E')
        super().method()


class F(A, B1):
    pass
    # def method(self):
    #     print('called in class F')
    #     super().method()


if __name__ == '__main__':
    b = B()
    b.method()  # A().method()
    C().method()

    D().method()  # called in D and in C
    E().method()  # called in E and in A

    print(F.mro())
    F().method()
    F().unique_method()
    