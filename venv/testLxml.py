from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive" name="zhangsan"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
# print(result.decode('utf-8'))

result1 =  html.xpath('//*')
# print(result1)

# 获取所有li下的a节点
list_li = html.xpath('//li/a')
# print(list_li)
# print(list_li[0])
# print(list_li[3])
#
#
# # 获取ul直接子节点
zhijie_child = html.xpath('//ul/*')
# print(zhijie_child)
# # print(zhijie_child[0])

# 选中 href 是 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class 属性
father_attr = html.xpath('//a[@href="https://ask.hellobi.com/link3.html"]/../@name')
# print(father_attr)

# 选取 class 为 item-1 的 li 节点
class_attr = html.xpath('//li[@class="item-0"]')
# print(class_attr)
# 选取 class 为 item-1 的 li节点里面a标签的文本
class_attr = html.xpath('//li[@class="item-0"]/a/text()')
# print(class_attr)

# 属性获取
attr_href = html.xpath('//li/a/@href')
# print(attr_href)

# 查询第一个节点内容
first_node_value = html.xpath('//li[1]/a//text()')
# print(first_node_value)

# 查询最后一个节点内容
last_node_value = html.xpath('//li[last()]/a//text()')
# print(last_node_value)

# 查询倒数第二个节点内容
last_sec_node_value = html.xpath('//li[last()-1]/a//text()')
# print(last_sec_node_value)

# 查询序数小于2的内容
xh_xy_node_value = html.xpath('//li[position() < 4]/a//text()')
# print(xh_xy_node_value)

# 查询第一个节点的所有祖先节点
ancestor_all_father = html.xpath('//li[1]/ancestor::*')
# print(ancestor_all_father)

# 查询第一节点所有孩子节点
child_all_first = html.xpath('//li[1]/child::*')
# print(child_all_first)

# 查询第一节点所有div直接孩子节点
divnode_all_first = html.xpath('//li[1]/ancestor::div')
# print(divnode_all_first)

attr_all_first = html.xpath('//li/attribute::*')
# print(attr_all_first)

# 查询第一节点所有子孙节点
zisun_all_first = html.xpath('//li[1]/descendant::*')
print(zisun_all_first)



