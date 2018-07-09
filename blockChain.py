#!/usr/bin/env python
#coding=utf-8

class Blockchain(object):
	# 定义两个列表，用于记录区块链及交易信息

	def __init__(self)
		self.chain = []
		self.current_transaction = []

		def new_block(self):
			# 创建一个新的 Block 区块，并添加到区块链中
			pass
		def new_transaction(self):
			#在交易中添加一个交易信息
			pass
		@staticmethod
		def hash(block):
			# 通过 Hash 算法返回区块的Hash 值
			pass
	'''
	6.接下来我们完善区块链创建区块的方法，想一想在区块链创世之初，还没有任何区块的时候，这个时候区块链刚刚被创建，
	因此我们需要创建区块的时候，制定一个创世区块，并给他添加一个工作量证明，先来理一下创建新区块需要做的哪些事情，
	需要记录前面一个区块的hash 地址，需要记录工作量的证明，没有工作量，谁给你发工资，类似于公司里的考核，接下来我们
	就来实现 new——block 方法
	'''

	def  new_block(self,proof,previous_hash=None):

		'''
		生成新块
		:param proof:<int>工作量证明，他是一个工作量算法对应的一个值
		:param previous_hash:(Optional)<str>前一个区块的 hash 值
		:return:<dict> 返回一个新的块，这个块 block 是一个字典结构
		'''
		block = {
			# 新的 block 对应的 index(当前区块长度+1)
			'index':len(self,chain) + 1
			# 时间戳，记录区块创建的时间(系统时间)
			'timestamp':time(),
			# 记录当前的交易记录，即通过 new_transactions 创建的交易,记录在这个新的 block 里
			'transactions':self.current_transaction,
			# 工作量证明
			'proof':proof
		     # 前一个 block 对应的 hash 值
			'previous_hash':previous_hash or self.hash(self.chain[-1]),
		}

		# 重置当前的交易，用于记录下一次交易
		self.current_transaction = []
		# 将新生成的 block 添加到 block 列表中
		self.chain.append(block)
		# 返回创新的 block
		return block


'''	前面说了在区块链创建之初，需要先创建创世块，这个创世块应该在哪个位置被创建呢？没错，就是和区块链一起创建，自然是在__init__方法
	中，接下来我们看看__init__方法。'''
	def __init__(self)
		self.current_transaction = []
		self.chain = []
		






		pass

