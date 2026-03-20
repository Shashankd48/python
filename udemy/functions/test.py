loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    total = 0
    is_bonus_applied = False
    
    for tr in transactions:
        total += tr
    
    
    def apply_bonus():
        nonlocal total
        
        if total > 1000:
            total += 50
    
    apply_bonus()
    
    
    global loyalty_points
    
    loyalty_points += total // 100
        
    
    return total

print(process_transactions([400, 700, 400]),loyalty_points)