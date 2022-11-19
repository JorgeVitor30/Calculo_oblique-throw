from math import sin,cos, tan, pi

g = 10

class Lancamento:
  def __init__(self, v0, ang):
      self.v0 = v0
      self.ang = ang*pi/180 
      self.t = (2*self.v0*sin(self.ang)) / g
    
  def __repr__(self):
        return (
        'Informações:\n'
        f'V0: {self.v0} m/s\n'  
        f'ang: {self.ang:.2f} rad')
    
  def altura_max(self):
    return f'{(self.v0 ** 2) * (sin(self.ang)**2) / (2 * g):.2f}'

  def amplitude(self):
    return f'{self.v0 * cos(self.ang) * self.t:.2f}'
    
  def equacao_trajetoria(self, s):
    y = tan(self.ang)*s - (g*(s**2))/(2*(self.v0**2)*(cos(self.ang)**2))

    return f"O objeto se encontra nas coordenadas ({s:.2f}, {y:.2f})"

pedra = Lancamento(v0=10, ang=45) #Velocidade->m/s ---- Ângulo->Graus

print(pedra)
print()
print(f'Tempo Total: {pedra.t:.2f} s')
print(f'Alcance: {pedra.amplitude()} m')
print(f'Altura Máxima: {pedra.altura_max()} m')
print(pedra.equacao_trajetoria(5))
