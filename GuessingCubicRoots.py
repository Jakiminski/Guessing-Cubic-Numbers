#!/usr/bin/env python
# coding: utf-8

# NOTE: call python3, if it's not your default python env
from random import *

MAX_TENTATIVAS = 3

def cubic(x):

	print('X^3 = {}.'.format(x**3), end='\t')
	y = int(input('Qual o valor de X inteiro?\t'))
	return [x**3, y == x, y] 

if __name__ == '__main__':
	
	i = MAX_TENTATIVAS
	rightAnswers = 0
	score = 0
	while (True):
		if i == MAX_TENTATIVAS: 
			x = randint(1,100)	
		cube, flag, y = cubic(x)
		
		if not flag and i > 0:
			i -= 1
			print('Errou!', end=' ' if i!=0 else '\n')
			if i!=0:
				print('Tente novamente.')
			print('Tentativas Restantes: ' + str(i) + '/' + str(MAX_TENTATIVAS) + '\n')
			if i == 0:
				print('\n------------- RESULTADOS -------------\n')
			
		elif flag:
			print('Acertou! A raíz de {} é {}'.format(cube, x))
			rightAnswers += 1
			score += i
			i = MAX_TENTATIVAS
			print('{} respostas certas'.format(rightAnswers), end=' ')
			print('e {} pontos.\n'.format(score))
		
		if i == 0:
			print('A raíz de {} é {}.\n'.format(cube, x))
			break
	
	print('Total de acertos: {} pts.'.format(rightAnswers), end='\t')
	print('Pontuação total: {} pts.'.format(score))
	