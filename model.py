def process_results(data):
    # print(data)
    output={"earth_count":0,"fire_count":0,"water_count":0,"air_count":0}
    for key in data:
        if data[key]== "earth":
            output["earth_count"]+=1
        elif data[key]=="air":
            output["air_count"]+=1
        elif data[key]=="water":
            output["water_count"]+=1
        elif data[key]=="fire":
            output["fire_count"]+=1
    # output=[]
    # for key in data:
    #     if data[key]== "earth":
    #         output.append("earth")
    #     elif data[key]== "air":
    #         output.append("air")
    #     elif data[key]== "water":
    #         output.append("water")
    #     elif data[key]== "fire":
    #         output.append("fire")
    return output
        
    # return output
    # max_value=0
    # for value in output.values():
    #     if value >= max_value:
    #         max_value = value
    #     return max_value

def most_frequent(data):
    output=process_results(data)
    maximum = 0
    element = ""
    for key in output:
        if output[key] > maximum:
            maximum=output[key]
            element = key
    return element 

    # max_value = max(set(output), key = output.count())
    # num_earth=output.count("earth")
    # num_air=output.count("air")
    # num_fire=output.count("fire")
    # num_water=output.count("water")
    # print(max_value)
    # return max_value
    
def bender_selection(max_value):
    if max_value == "earth_count":
        return "an Earthbender! You are hardset in your beliefs, and have no problems standing your ground. You understand the value of hard work and know that if you set goals and map out a plan for them, you can accomplish anything."
        
    elif max_value == "air_count":
        return "an Airbender! You are very in touch with your emotions- because of this, it's easy for you to let go when you feel like you've been wronged. You enjoy the simple things in life, having no problem getting by with little. You feel strong connections with nature and enjoy spending time outdoors."
    elif max_value == "water_count":
        return "a Waterbender! You are very much a 'go with the flow' kind of person. You are in touch with your emotions, and for that reason, get along with people very well. You try to remain flexible in all situations, and are hapiest when you can creatively problem solve. You feel very connected to family and community. "
    elif max_value == "fire_count":
        return "a Firebender! You acknowledge that you can be a little hot headed, and your spontaneity has gotten you in trouble before. You feel very intensely and have trouble holding back, but can also reflect on the effect your words have on others. You believe strongly in order and rules, but know when to bend them."

def img_selection(max_value):
    if max_value == "earth_count":
        return "/static/images/earth_nation.jpg"
    elif max_value == "air_count":
        return "/static/images/air_nation.jpg"
    elif max_value == "water_count":
        return "/static/images/water_nation.jpg"
    elif max_value == "fire_count":
        return "/static/images/fire_nation.jpg"
    
 
        

