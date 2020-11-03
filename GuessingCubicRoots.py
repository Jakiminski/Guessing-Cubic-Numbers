from random import *

MAX_TENTATIVAS = int(3)
def cubic(x):

	print('X^3 = {}.'.format(x**3), end='\t')
	y = int(input('Qual o valor de X inteiro?'))
	return [x**3, y == x, y] 


if __name__ == '__main__':
	
	i = MAX_TENTATIVAS
	
	while (i>0):
		x = randint(1,100)	
		cube, flag, y = cubic(x)
		print('Acertou! A raíz de {} é {}'.format(cube, x) if flag else 'Errou! A raíz de {} é {}.'.format(cube, x))
		i = i-1 if not flag else MAX_TENTATIVAS
		print('Tentativas Restantes: ' + i + '/' + MAX_TENTATIVAS)