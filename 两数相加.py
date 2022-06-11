class ListNode:
	def __init__(self,val=0,next=None):
		self.val=val
		self.next=next

a=ListNode([1,7,9])

print(a.next)

class solution:
	def add(self ,l1:ListNode,l2:ListNode) ->ListNode:

		a=b=ListNode(None)
		add=0

		while l1 or l2 or add :
			add=add+ (l1.val if l1 else 0 )+ (l2.val if l2 else 0 )
			b.next=ListNode(add%10)
			add = add // 10
			b=b.next
			l1=l1.next if l1 else None
			l2=l2.next if l2 else None
		return a.next

