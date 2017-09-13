#leetcodeDP题目解法思路汇总
'''
53. Maximum Subarray
思路参考：http://blog.csdn.net/linhuanmars/article/details/21314059
核心思路：局部最优和全局最优解法
'''

'''
198. House Robber
题意理解：
stash[stæʃ] n.藏匿处；藏匿物 vt.存放；贮藏 vi.存放；
constraint [kən'streɪnt] n.约束；局促，态度不自然；强制
adjacent[ə'dʒeɪs(ə)nt] n.临近的，毗邻的
思路参考：
核心思路：
递推关系：
	求解该问题子问题的最大值问题
	maxV[i] = max(maxV[i-1],maxV[i-2]+num[i])
	更具体的：
		f(0) = num[0]
		f(1) = max(num[0],num[1])
		f(2) = max(f(1),f(0)+num[2])
		f(3) = max(f(2),f(1)+num[3])
		f(k) = max(f(k-1),f(k-2)+num[k])
		
代码：

'''