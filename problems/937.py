"""
937. Reorder Data in Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Solution:

Have two arrays: a letter_logs and a digit_logs
Loop through the logs and split each log on the space character
Determine if the next item after the identifier is a numeric or alpha
If its numeric add the log to the digit_logs
Otherwise Perform an insertion sort on the letter_logs on where to insert the new log.

Runtime: O(N^2)
Space: O(N)
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit_logs = []
        letter_logs = []
        for log in logs:
            splitted = log.split(" ")
            identifier = splitted[0]
            
            next_item = splitted[1]
            
            if next_item.isnumeric():
                digit_logs.append(log)
            else:
                if len(letter_logs) == 0:
                    letter_logs.append(log)
                else:
                    for i in range(len(letter_logs)):
                        to_be_inserted = splitted[1:]
                        current = letter_logs[i]
                        current_splitted = current.split(" ")
                        compare_with = current_splitted[1:]
                        
                        
                        to_be_inserted_string = '-'.join(to_be_inserted)
                        compare_with_string = '-'.join(compare_with)
                        
                        
                        if to_be_inserted_string > compare_with_string:
                            if i == len(letter_logs) - 1:
                                letter_logs.append(log)
                            continue
                        else:
                            letter_logs.insert(i, log)
                            break
                            
        return letter_logs + digit_logs