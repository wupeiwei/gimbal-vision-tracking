//
// Created by jwpw0 on 2026/9/18.
//

#ifndef GIMBAL_VISION_TRACKING_UART_H
#define GIMBAL_VISION_TRACKING_UART_H

#include <stdint.h>


int ring_put(uint8_t b);

int ring_get(uint8_t *b);

uint16_t ring_count(void);

/* 发送一个以 \0 结尾的字符串（不含 \0） */
void uart_send_str(const char *s);

#endif //GIMBAL_VISION_TRACKING_UART_H
