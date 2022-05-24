import time
import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')

ENA_low = board.get_pin('d:6:p')
ENB_low = board.get_pin('d:5:p')
IN1_low = board.get_pin('d:7:o')
IN2_low = board.get_pin('d:4:o')
IN3_low = board.get_pin('d:3:o')
IN4_low = board.get_pin('d:2:o')

ENA_high = board.get_pin('d:11:p')
ENB_high = board.get_pin('d:10:p')
IN1_high = board.get_pin('d:13:o')
IN2_high = board.get_pin('d:12:o')
IN3_high = board.get_pin('d:9:o')
IN4_high = board.get_pin('d:8:o')

# forward
IN1_low.write(1); IN2_low.write(0); IN3_low.write(1); IN4_low.write(0)
IN1_high.write(1); IN2_high.write(0); IN3_high.write(1); IN4_high.write(0)
ENA_low.write(1); ENB_low.write(1)
ENA_high.write(1); ENB_high.write(1)
time.sleep(4)

for i in range(0, 9):
    # right
    IN1_low.write(1); IN2_low.write(0); IN3_low.write(0); IN4_low.write(1)
    IN1_high.write(1); IN2_high.write(0); IN3_high.write(0); IN4_high.write(1)
    ENA_low.write(0.75); ENB_low.write(0.75)
    ENA_high.write(0.75); ENB_high.write(0.75)
    time.sleep(0.5)
    
    # stop
    IN1_low.write(1); IN2_low.write(1); IN3_low.write(1); IN4_low.write(1)
    IN1_high.write(1); IN2_high.write(1); IN3_high.write(1); IN4_high.write(1)
    ENA_low.write(1); ENB_low.write(1)
    ENA_high.write(1); ENB_high.write(1)
    time.sleep(0.5)
    
    # forward
    IN1_low.write(1); IN2_low.write(0); IN3_low.write(1); IN4_low.write(0)
    IN1_high.write(1); IN2_high.write(0); IN3_high.write(1); IN4_high.write(0)
    ENA_low.write(0.75); ENB_low.write(0.75)
    ENA_high.write(0.75); ENB_high.write(0.75)
    time.sleep(0.5)

# forward
IN1_low.write(1); IN2_low.write(0); IN3_low.write(1); IN4_low.write(0)
IN1_high.write(1); IN2_high.write(0); IN3_high.write(1); IN4_high.write(0)
ENA_low.write(1); ENB_low.write(1)
ENA_high.write(1); ENB_high.write(1)
time.sleep(4)

for i in range(0, 9):
    # right
    IN1_low.write(1); IN2_low.write(0); IN3_low.write(0); IN4_low.write(1)
    IN1_high.write(1); IN2_high.write(0); IN3_high.write(0); IN4_high.write(1)
    ENA_low.write(0.75); ENB_low.write(0.75)
    ENA_high.write(0.75); ENB_high.write(0.75)
    time.sleep(0.5)
    
    # stop
    IN1_low.write(1); IN2_low.write(1); IN3_low.write(1); IN4_low.write(1)
    IN1_high.write(1); IN2_high.write(1); IN3_high.write(1); IN4_high.write(1)
    ENA_low.write(1); ENB_low.write(1)
    ENA_high.write(1); ENB_high.write(1)
    time.sleep(0.5)
    
    # forward
    IN1_low.write(1); IN2_low.write(0); IN3_low.write(1); IN4_low.write(0)
    IN1_high.write(1); IN2_high.write(0); IN3_high.write(1); IN4_high.write(0)
    ENA_low.write(0.75); ENB_low.write(0.75)
    ENA_high.write(0.75); ENB_high.write(0.75)
    time.sleep(0.5)

# stop
IN1_low.write(1); IN2_low.write(1); IN3_low.write(1); IN4_low.write(1)
IN1_high.write(1); IN2_high.write(1); IN3_high.write(1); IN4_high.write(1)
ENA_low.write(1); ENB_low.write(1)
ENA_high.write(1); ENB_high.write(1)
time.sleep(0.5)