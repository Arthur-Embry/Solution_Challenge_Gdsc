from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel, PositiveInt 
import openai
import os


openai.api_key = os.environ["OPENAI_API_KEY"]

# Completed goals: number of goals completed by user 
# Goal Streak: number of days a goal is completed consecutively
# Open Streak: number of days user opens the app consecutively 
# Community Engagement: user's interaction with community features
# Level: what level the user is on, based on number of points earned
class points_params(BaseModel):
    completed_goals: PositiveInt = 0 
    goal_streak: PositiveInt = 0 
    open_streak: PositiveInt = 0 
    community_engagement: PositiveInt = 0
    level: int = 1

# DECIDE ON POINT VALUES AND CHANGE!
def points_run(params: points_params):
    goal_points = params.completed_goals * 10
    
    streak_points = params.goal_streak * 20
    
    if params.app_open_streak >= 7: 
        streak_points += params.open_streak * 5
    else:
        streak_points += params.open_streak
    
    total_points = goal_points + streak_points
    
    if total_points >= 100:
        params.level = 5
    elif total_points >= 75:
        params.level = 4
    elif total_points >= 50:
        params.level = 3
    elif total_points >= 25:
        params.level = 2
    else:
        params.level = 1
    
    return params

# Leaderboard type: default is all users, can change to friends
# Time range: points earned within a certain amount of time 
# Limit: number of users shown 
class leaderboard_params(BaseModel):
    leaderboard_type: str = "All Users" 
    time_range: str = "Current Month"
    limit: int = 10 


def leaderboard_run(params: leaderboard_params):
    if params.leaderboard_type == "All Users":
        all_users = get_all_users() #database query??
        user_points = {user: points_run(user) for user in all_users}
        sorted_users = sorted(user_points.items(), key=lambda x: x[1], reverse=True)
        top_users = sorted_users[:params.limit]
        leaderboard = [{"user": user, "points": points} for user, points in top_users]
        
    elif params.leaderboard_type == "Friends":
        user_friends = friends_run(params.user_id)  #database query
        friend_points = {friend: points_run(friend) for friend in user_friends}  
        sorted_friends = sorted(friend_points.items(), key=lambda x: x[1], reverse=True)
        top_friends = sorted_friends[:params.limit]
        leaderboard = [{"friend": friend, "points": points} for friend, points in top_friends]
      
    else:
      raise ValueError ("Invalid leaderboard type")

    return leaderboard

# user_ID: unique identifier for user
# friend_ID: unique identifier for other user, user's friend
# room_code: similar to among us or kahoot
class friends_params(BaseModel):
    user_ID: int
    friend_ID: int
    room_code: int 

def friends_run(params: friends_params):
    
    
class metadata_params(BaseModel):
    #TODO: implement params [ASK: What metadata is relevant]
    pass

def metadata_run(params: metadata_params):
    #TODO: implement function
    pass

# categories include mental health, physical health, misc. 
# difficulty_level: allow the user to decide how difficult it is for them
class goals_params(BaseModel):
    goal_name: str
    goal_description: str 
    goal_category: str
    point_value: int
    difficulty_level: str
    is_completed: bool

def goals_run(params: goals_params, is_completed: bool):
    goals = params.goal_name
    if is_completed:
      points = 10
    else:
      points = 0

    response_data = {"points": points}
    return response_data

class audio_upload_params(BaseModel):
    #TODO: implement params [ASK: like length? what are we doing with this]
    pass

def audio_upload_run():
    #TODO: implement function
    pass