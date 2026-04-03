import random  
  
def embryo_quality_score(stage, morphology):  
    score = 0  
  
    if stage == "Blastocyst":  
        score += 5  
    elif stage == "Cleavage":  
        score += 3  
  
    if morphology == "Good":  
        score += 5  
    elif morphology == "Average":  
        score += 3  
    else:  
        score += 1  
  
    return score  
  
  
def simulate_freezing(temp, cryoprotectant):  
    survival_rate = 0  
  
    if temp <= -196:  
        survival_rate += 50  
  
    if cryoprotectant == "DMSO":  
        survival_rate += 30  
    elif cryoprotectant == "Glycerol":  
        survival_rate += 20  
  
    return survival_rate + random.randint(0, 20)  
  
  
def thawing_success(rate):  
    if rate > 70:  
        return "High Survival"  
    elif rate > 40:  
        return "Moderate Survival"  
    else:  
        return "Low Survival"  
