# HW2

Name: 赵宇飞    Student ID: 2200017812     Server ID: leb36     Group number: G07A

## Editing steps, commands and time

### table1a

The given table1b has five repeated lines and have different patterns from the required table1a. I did not find a fast way to edit this, so I just delete most of the contents by hand. `:%s/- //g` is used to delete the -'s, and other contents are edited by hand, using `i` to enter insert mode. I finished it in 3 minutes.

### 0319a

`dd` is used to delete the trash lines. I use `dw` to delete single word, `:%s/[()]//g` to delete parentheses, `:%s/^I--//g` and `:%s/^I否//g` to delete the trash columns, and add table titles manually. I finished it in 2 minutes.

### hba208a

`:%s/Hemoglobin subunit alpha//g` is used to delete the common trash words, and some additional editings are by hand. I finished it for less than 5 minutes.

