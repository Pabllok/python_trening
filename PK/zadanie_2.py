# Fp=0.5ρ*V2*A*Cx

class Plane:

    def __init__(self, brand="no brand", model="no model"):
        self.brand = brand
        self.model = model

    def showplane(self):
        print("Plane: ", self.brand, self.model, )


class FpCalc:

    def __init__(self, p, v, A, Cx):
        self.p = p
        self.v = v
        self.A = A
        self.Cx = Cx

    def fp(self):

        x = 0.5 * self.p * self.v ** 2 * self.A * self.Cx
        return x

plane_1 = Plane("Black Star", "F45")
plane_1.showplane()
fpplane_1 = FpCalc(100, 100, 80, 5)
print("Drag Force = ", fpplane_1.fp())
