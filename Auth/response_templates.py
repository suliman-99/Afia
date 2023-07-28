from Auth.models import User


def user_dict(user:User):
    return {
        'user': {
            'id': user.id,
            'email': user.email,
            'email_verified': user.email_verified,
            'role': user.role,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
            'birth_date': user.birth_date,
            'gender': user.gender,
            'photo': str(user.photo),
            'city': user.city,
            'blood_type': user.blood_type,
            'length': user.length,
            'weight': user.weight,
            'chronic_disease': user.chronic_disease,
            'genetic_disease': user.genetic_disease,
            'other_info': user.other_info,
            'license': str(user.license),
            'available_for_meeting': user.available_for_meeting,
            'specialization': user.specialization,
        }
    }
    
    
def verified_user_dict(user, refresh, access):
    ret = user_dict(user)
    ret.update({
        'refresh': refresh,
        'access': access,
    })
    return ret

