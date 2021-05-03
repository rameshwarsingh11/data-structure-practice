'''

Given an array of the revenue on each day, and an array of milestones a company wants to reach, return an array containing the days on which the company reached every milestone.
Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)
Input
revenues is a length-N array representing how much revenue company made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
Output
Return a length-K array where K_i is the day on which company first had milestones[i] total revenue. If the milestone is never met, return -1.
Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, company has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that the compnay has >= $200 of total revenue.
'''


from queue import Queue



def getMilestoneDays(revenues, milestones):
  q = Queue(maxsize=len(revenues))
  for revenue in revenues:
    q.put(revenue)

  total = 0

  output = []
  days = 0

  milestones.sort()
  milestone_met = False
  for milestone in milestones:
    while total < milestone and not q.empty():
      
      revenue = q.get()
      total += revenue
      #print('Total ', total)
      days += 1

    if total >= milestone:
      #print('Milestone', milestone, ' achieved in', days, 'days')
      milestone_met = True
      output.append(days)

    if milestone_met == False:
      print('Sorry, milestone not met.')
      return -1

  return output


revenues = [100, 200, 300, 400, 500]
milestones = [300, 800, 1000, 1400]
print(getMilestoneDays(revenues, milestones))

revenues_2 = [700, 800, 600, 400, 600, 700]
milestones_2 = [3100, 2200, 800, 2100, 1000]
print(getMilestoneDays(revenues_2, milestones_2))
