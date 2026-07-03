def check_symptoms(fever, cough, headache, bodypain):

    if fever.lower()=="yes" and cough.lower()=="yes":
        return "Flu"

    elif fever.lower()=="yes" and bodypain.lower()=="yes":
        return "Dengue"

    elif headache.lower()=="yes":
        return "Migraine"

    elif cough.lower()=="yes":
        return "Cold"

    else:
        return "No major disease found"