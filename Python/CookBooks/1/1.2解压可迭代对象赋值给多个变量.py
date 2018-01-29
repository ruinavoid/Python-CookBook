def drop(grades):
    first, *middle, last = grades
    return sum(middle)


numArr = [7, 5, 3, 1, 6, 3, 5, 7, 9]
summ = drop(numArr)
print(str(summ) + '\n')

record = ('Dave', 'dave@exmple.com', '773-555-1212', '847-555-1212')
name, email, *phone_number = record
print(name, email, phone_number)

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(sales_record) / len(sales_record)


def comparison(compA, compB):
    if compA > compB:
        return compA
    else:
        return compB

print(comparison(trailing_avg,current_qtr))

records = [ ('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
username,*feilds,home,sh = line.split(':')
print(username)
print(home)
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_,(*_, year) = record
print(name)
print(year)

items = [1,10,7,4,5,9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head

print(sum(items))
