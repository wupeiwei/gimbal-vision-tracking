//
// Created by jwpw0 on 2026/9/18.
//

#include "uart.h"

#include <string.h>
#include "usart.h"

#define RING_SIZE 128U

static volatile uint8_t ring_buf[RING_SIZE];
static volatile uint16_t ring_head = 0;
static volatile uint16_t ring_tail = 0;
static volatile uint32_t ring_overflow = 0;

int ring_put(uint8_t b) {
    uint16_t next = ring_head + 1U;
    if (next >= RING_SIZE) {
        next = 0U;
    }

    if (next == ring_tail) {
        ring_overflow++;
        return 0;
    }

    ring_buf[ring_head] = b;
    ring_head = next;
    return 1;
}

uint16_t ring_count(void) {
    uint16_t head = ring_head;
    uint16_t tail = ring_tail;

    if (head >= tail) {
        return (uint16_t) (head - tail);
    }
    return (uint16_t) (head + RING_SIZE - tail);
}

int ring_get(uint8_t *b) {
    if (ring_tail == ring_head) {
        return 0;
    }

    *b = ring_buf[ring_tail];
    ring_tail++;
    if (ring_tail >= RING_SIZE) {
        ring_tail = 0U;
    }
    return 1;
}

void uart_send_str(const char *str) {
    int len = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        len++;
    }
    HAL_UART_Transmit(&huart1, (uint8_t *) str, len, 1000);
}
