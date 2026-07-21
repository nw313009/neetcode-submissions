from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    score_list = []
    for name,score in scores:
        score_list += [score]
    
    max_val = max(score_list)
    for name,score in scores:
        if(max_val == score ):
            return name
        
        

        #print(f"name: {name}, score: {score}")
        #score_list += [score]
        #max_score = max(score_list)
        #print(max_score)
    
    
        
        
        




        
        
    
    
    
    
        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
