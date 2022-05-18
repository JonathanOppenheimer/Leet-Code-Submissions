/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct double_list {
    int val;
    struct double_list *next;
    struct double_list *prev;
};



bool isPalindrome(struct ListNode* head){

    struct ListNode* head_head = head; 
    struct double_list* doubly = malloc(sizeof(struct double_list));
    struct double_list* doubly_head = doubly; 
    
    while(head != NULL) {
        doubly->val = head->val; 
        struct double_list* temp = malloc(sizeof(struct double_list)); 
        doubly->next = temp; 
        temp->prev = doubly; 
        doubly = doubly->next; 
        
        head=head->next; 
    }
    head = head_head; 
    doubly = doubly->prev; 
    
    bool palindrome = true; 
    while(head != NULL) {
        if(head->val != doubly->val) {
            palindrome = false; 
        }
        head = head->next; 
        doubly = doubly->prev; 
    }
    
    return palindrome; 
    
    
//     int length = 0; 
//     struct ListNode * maintain_head = head; 
//     while(head != NULL) {
//         head = head->next;
//         length++;
//     }
//     head = maintain_head; 
    
//     struct ListNode* reversed = malloc(sizeof(struct ListNode));
//     assert(reversed != NULL);
//     reversed->val = 0; 
//     reversed->next = NULL;
//     struct ListNode * maintain_head_reversed = reversed; 
    
//     int count_down = length - 1; 
//     while(count_down >= 0) {
//         for(int i = count_down; i > 0; i--) {
//             head=head->next; 
//         } 
//         reversed->val = head->val; 
//         printf("%d\n", reversed->val); 
//         struct ListNode* next = malloc(sizeof(struct ListNode));
//         assert(next != NULL);
//         next->val = 0; 
//         next->next = NULL;
//         reversed->next = next; 
//         reversed = reversed->next; 
//         head = maintain_head; 
//         count_down--; 
//     }
//     reversed = maintain_head_reversed; 
   
//     bool all_matching = true; 
//     for(int i=0; i<length; i++) {
//         if(head->val != reversed->val) {
//             all_matching = false;
//         }
//         head = head->next; 
//         reversed = reversed->next;
//     }
//     return all_matching; 
}