/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* l1_head = l1; 
    int l1_length = 0;
    while(l1 != NULL) {
        l1_length++; 
        l1 = l1->next; 
    }
    l1 = l1_head; 
    
    struct ListNode* l2_head = l2; 
    int l2_length = 0; 
    while(l2 != NULL) {
        l2_length++;
        l2 = l2->next; 
    }
    l2 = l2_head; 
    
    int* l1_array = malloc(sizeof(int) * l1_length); 
    for(int i=0; i<l1_length; i++) {
        l1_array[i] = l1->val; 
        l1 = l1->next; 
    }
    l1 = l1_head; 
    
    int* l2_array = malloc(sizeof(int) * l2_length); 
    for(int i=0; i<l2_length; i++) {
        l2_array[i] = l2->val; 
        l2 = l2->next; 
    }
    l2 = l2_head; 
    
    struct ListNode* final_sum = malloc(sizeof(struct ListNode)); 
    assert(final_sum != NULL);
    final_sum->val = 0; 
    final_sum->next = NULL;
    struct ListNode* final_sum_head = final_sum; 
    
    bool add_one = false; 
    int loop_end = l1_length >= l2_length ? l1_length : l2_length; 
    for(int i=0; i<loop_end; i++) {
        int sum = 0;   
        if(!(i > l1_length - 1)) {
            sum = sum + l1_array[i]; 
        }
         if(!(i > l2_length - 1)) {
            sum = sum + l2_array[i]; 
        } 
        if(add_one) {
            sum = sum + 1; 
            add_one = false; 
        }
        if(sum >= 10) {
            add_one = true; 
            sum = sum%10; 
        } 
        final_sum->val = sum;
        if(i != loop_end - 1) { 
            struct ListNode* nextNode = malloc(sizeof(struct ListNode)); 
            assert(nextNode != NULL);
            nextNode->val = 0; 
            nextNode->next = NULL;
            final_sum->next = nextNode; 
            final_sum = final_sum->next; 
        }
    }
    
    if(add_one) {
        struct ListNode* nextNode = malloc(sizeof(struct ListNode)); 
        assert(nextNode != NULL);
        nextNode->val = 1; 
        nextNode->next = NULL;
        final_sum->next = nextNode; 
        final_sum = final_sum->next; 
    }
    
    return final_sum_head; 
 }