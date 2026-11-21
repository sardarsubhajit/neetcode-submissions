class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        fleet = []
        for p, s in pair:
            time = (target - p) / s   # calculate the rem. time
            if not fleet:
                fleet.append(time)
            else:
                # if time required is more than the latest car fleet
                # then the car will be forming a new car fleet00
                if fleet[-1] < time:    
                    fleet.append(time)
        print(fleet)
        return len(fleet)