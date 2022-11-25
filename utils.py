#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import subprocess
import time

import vlc


def play_song(song_name):
    p = vlc.MediaPlayer(song_name)
    p.play()
    pass


def do_moves(moves, robot_ip, robot_port):
    # Here we execute all the given moves
    # in a Python2 environment.
    for move in moves:
        print(f"Executing: {move}... ", end="", flush=True)
        python2_command = f"python2 ./NaoMoves/{move}.py  {robot_ip} {robot_port}"
        start_move = time.time()
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        end_move = time.time()
        # print(process.stdout) # receive output from the python2 script
        print("done in %.2f seconds." % (end_move-start_move), flush=True)


def from_state_to_dict(state):
    params_dict = dict()
    for t in state:
        len_t = len(t)
        if len_t < 2:
            continue
        key = t[0]
        if len_t > 2:
            value = t[1:]
        else:
            value = t[1]
        if key not in params_dict:
            params_dict[key] = value
    return params_dict


def entropy(choreography):
    frequency_dict = {}
    for move in choreography:
        if move not in frequency_dict:
            frequency_dict[move] = 1
        else:
            frequency_dict[move] += 1
    result = 0.0
    for unique_move, frequency in frequency_dict.items():
        probability = frequency / len(choreography)
        result -= probability * math.log(probability, 2)
    return result