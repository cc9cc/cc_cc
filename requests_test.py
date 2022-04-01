# import requests
# import json
# import time
#
# s = requests.Session()
# data = {
#     "username" : "byhy",
#     "password" : "88888888",
# }
# s.post("http://127.0.0.1/api/mgr/signin", data=data)
# # params = {
# #     "action" : "list_customer",
# #     "pagesize" : "2",
# #     "pagenum" : "1",
# # }
# # rep = s.get("http://127.0.0.1/api/mgr/customers", params=params)
#
# # data1 = {
# #     "action":"add_customer",
# #     "data":{
# #         "name":"1",
# #         "phonenumber":"2551",
# #         "address":"武汉市桥西医院北路"
# #     }
# # }
# # rep = s.post("http://127.0.0.1/api/mgr/customers", json = data1)
#
# # data1 = {
# #     "action":"modify_customer",
# #     "id": 6,
# #     "newdata":{
# #         "name" : "武汉市桥北医院",
# #         "phonenumber" : "13345678888",
# #         "address" : "武汉市桥北医院北路"
# #     }
# # }
# #
# # rep = s.put("http://127.0.0.1/api/mgr/customers", json=data1)
#
# data1 = {
#     "action":"del_customer",
#     "id": 37
# }
# rep = s.delete("http://127.0.0.1/api/mgr/customers", json=data1)
# print(rep.status_code)
# print(rep.text)


# def intersect(nums1, nums2):
#     mid1 = 0
#     mid2 = 0
#     mid_result = []
#     result = []
#     for i in nums1:
#         if (i in nums2) and (i not in mid_result):
#             mid_result.append(i)
#     print(mid_result)
#     for j in mid_result:
#         for m in nums1:
#             if m == j:
#                 mid1 += 1
#         for n in nums2:
#             if n == j:
#                 mid2 += 1
#         # print(m,n)
#         min_value = min(mid1, mid2)
#         mid1 = 0
#         mid2 = 0
#         print(j, min_value)
#         for k in range(min_value):
#             result.append(j)
#     return result
#
# num1 = [4,9,5]
# num2 = [9,4,9,8,4]
# num3 = intersect(num1, num2)
# print(num3)



# result = [[1],[1,1],[1,2,1]]
# print(result[2])
# print(result[2][1])


# class Node:
#   # constructor
#   def __init__(self, data, next=None):
#     self.data = data
#     self.next = next

# 插在开头
# dummy = Node(0)
# dummy.next = head
# head = dummy
# return head

# 插在中间
# dummy = Node(0)
# dummy.next = prev.next
# prev.next = dummy

# 插在末尾
# dummy = Node(0)
# while head.next:
# 	head = head.next
# head.next = dummy
# dummy.next = None


# import sys
#
#
# # a = int(input())
# a=int(2000000014)
# zhishu = []
# while a > 1:
#     for i in range(2, int(a)+1):
#         if a % i == 0:
#             zhishu.append(i)
#             a = a/i
#             type(a)
#             break
# for x in zhishu:
#     print(x)



# def kkk(s):
#     length = len(s)
#     for i in range(length):
#         fenduan = s.split(s[i])
#         if len(fenduan) == 1:
#             return i
#     return -1


# def canConstruct(ransomNote, magazine):
#     ransomNoteDict = {}
#     magazineDict = {}
#     for i in range(len(ransomNote)):
#         if ransomNote[i] in ransomNoteDict:
#             ransomNoteDict[ransomNote[i]] += 1
#         else:
#             ransomNoteDict[ransomNote[i]] = 1
#     for j in range(len(magazine)):
#         # magazineDict[magazine[i]] += 1
#         if magazine[i] in magazineDict:
#             magazineDict[magazine[i]] += 1
#         else:
#             magazineDict[magazine[i]] = 1
#     flag = True
#     for k in ransomNoteDict:
#         if k in magazineDict and ransomNoteDict.get(k) == magazineDict.get(k):
#             flag = True
#         else:
#             flag = False
#     return flag
#
# l = canConstruct('aa', 'aab')
# print(l)

# A single node of a singly linked list
# class ListNode:
#   # constructor
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
#
# def mergeTwoLists( list1: ListNode, list2: ListNode):
#     dummy = ListNode(-1)
#     dummy.next = list1
#     while list1 != None or list2 != None:
#         print(type(list1))
#         if list2.val > list1.val:
#             list1 = list1.next
#             continue
#         else:
#             mid_node = ListNode(list2.val)
#             mid_node.next = list1.next
#             list1.next = mid_node
#         list2 = list2.next
#     if list1 == None:
#         list1.next = list2
#     return dummy.next
#
#
# x = mergeTwoLists([1,2,3], [1,3,4])


# def quchong(list1):
#     list2 = []
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#     list2.sort()
#     for j in list2:
#         print(j)
#
#
# n = int(input())
# while True:
#     list1 = []
#     for i in range(n):
#         list1.append(int(input()))
#     quchong(list1)
#     n = int(input())
# import  collections
#
# import collections
#
#
# while True:
#     try:
#         str1 = input()
#         shuliang = collections.Counter(str1)
#         minNum = min(sorted(shuliang.values()))
#         for j in shuliang:
#             if shuliang.get(j) == minNum:
#                 str1 = str1.replace(j, "")
#         print(str1)
#     except:
#         pass


