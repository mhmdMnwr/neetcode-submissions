class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        mx = 0
        
        for char in s:
            # إذا كان الحرف موجوداً مسبقاً، نحذف كل ما قبله بما في ذلك الحرف المكرر القديم
            if char in seen:
                # نجد موقع الحرف المكرر
                index = seen.index(char)
                # نحذف الحرف المكرر وكل العناصر التي تسبقه
                del seen[:index + 1]
            
            # نضيف الحرف الحالي دائماً
            seen.append(char)
            # نحدث القيمة القصوى لطول السلسلة الفرعية
            mx = max(mx, len(seen))
            
        return mx
