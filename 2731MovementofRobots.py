"""
Some robots are standing on an infinite number line with their
initial coordinates given by a 0-indexed integer array nums and will start
moving once given the command to move. The robots will move a unit distance each second.

You are given a string s denoting the direction in which robots will move on
command. 'L' means the robot will move towards the left side or negative side of
the number line, whereas 'R' means the robot will move towards the
right side or positive side of the number line.

If two robots collide, they will start moving in opposite directions.

Return the sum of distances between all the pairs of robots d seconds after the command. Since the sum can be very large, return it modulo 109 + 7.

Note:

    For two robots at the index i and j, pair (i,j) and pair (j,i) are considered the same pair.
    When robots collide, they instantly change their directions without wasting any time.
    Collision happens when two robots share the same place in a moment.
        For example, if a robot is positioned in 0 going to the right and another is positioned in 2 going to the left, the next second they'll be both in 1 and they will change direction and the next second the first one will be in 0, heading left, and another will be in 2, heading right.
        For example, if a robot is positioned in 0 going to the right and another is positioned in 1 going to the left, the next second the first one will be in 0, heading left, and another will be in 1, heading right.



Example 1:

Input: nums = [-2,0,2], s = "RLL", d = 3
Output: 8
Explanation:
After 1 second, the positions are [-1,-1,1]. Now, the robot at index 0 will move left, and the robot at index 1 will move right.
After 2 seconds, the positions are [-2,0,0]. Now, the robot at index 1 will move left, and the robot at index 2 will move right.
After 3 seconds, the positions are [-3,-1,1].
The distance between the robot at index 0 and 1 is abs(-3 - (-1)) = 2.
The distance between the robot at index 0 and 2 is abs(-3 - 1) = 4.
The distance between the robot at index 1 and 2 is abs(-1 - 1) = 2.
The sum of the pairs of all distances = 2 + 4 + 2 = 8.

Example 2:

Input: nums = [1,0], s = "RL", d = 2
Output: 5
Explanation:
After 1 second, the positions are [2,-1].
After 2 seconds, the positions are [3,-2].
The distance between the two robots is abs(-2 - 3) = 5.



Constraints:

    2 <= nums.length <= 105
    -2 * 109 <= nums[i] <= 2 * 109
    0 <= d <= 109
    nums.length == s.length
    s consists of 'L' and 'R' only
    nums[i] will be unique.

"""

from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = nums.__len__()
        s = [-1 if i == 'L' else 1 for i in s]
        ns = [[nums[i], s[i]] for i in range(n)]
        ns.sort(key=lambda x: x[0])
        for _ in range(d):
            for i in range(n):
                ns[i][0] += ns[i][1]
            for i in range(n - 1):
                if ns[i][0] >= ns[i + 1][0]:
                    ns[i], ns[i + 1] = ns[i + 1], ns[i]
        return sum([i * (n - i) * (ns[i][0] - ns[i - 1][0]) for i in range(1, n)])

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:

        nums = sorted([num+(ord(ch)-79)//3*d            # Example : nums: [1,0,4,-5],  s:  'RLRL',  d:  2
                       for num, ch in zip(nums,s)])
                                                        #  nums = sorted([1+2, 0-2, 4+2, -5-2])
                                                        #       = [-7,-2,3,6]

        return sum(map(mul, nums, range(1-len(nums),    #  sum(map(mul, [[-7,-2,3,6],[-3,-1,1,3]]))
                       len(nums), 2)))%1000000007       #  sum((-7*-3)+(-2*-1)+(3*1)+(6*3))
                                                        #  return 44


A = Solution()
nums = [10421, 535686, -577310, -553499, -446384, -214024, 433375, 482991, -134992, 488334, -538986, -495046, 235593, 469077, -175854, -258011, 105550, -33819, -262675, -527552, -572600, 295456,
        -570995, -272723, -226772, -805, 429160, -351177, -463359, -35635, -42218, 532797, 328108, 397721, -519551, -382316, 374672, -149682, -551360, -429581, 577121, -262244, -240933, -472284,
        -311647, 575937, -515348, 571070, 431488, 508682, -581561, 528184, 294618, 458063, -480161, 520654, 506387, 45202, -532471, 504453, 62212, -86197, -351839, -355186, -197206, 236586, -241362,
        -113048, -294682, -142178, 539933, -167605, -183969, 4042, -253632, -387325, -266191, -369563, -82026, -111758, -285366, 392160, -440295, -336066, 165370, -257198, -21327, -349883, 161336,
        420300, 151952, -538676, -526180, 492660, -187458, -75064, -499415, 12995, -199088, -203047, 319206, 507945, 87339, -69057, 546163, 97641, -49327, -251455, 172750, -408543, -511831, -135448,
        162504, 320036, 400270, 394198, -78558, 536092, -539557, 545814, -310633, 216965, 109096, -211067, 439355, -332107, -104653, 546759, 245372, -483196, 550737, -540599, -258516, -364869,
        -345323, 437309, 92676, -59957, -227323, -441134, -148657, -300253, -116205, 55479, -459449, -269787, -304272, -256586, -570802, 497174, 513753, -230465, 50327, -172955, -550822, -475817,
        587138, -153441, -387182, -553339, 560009, 65247, 444673, 135420, -509690, 492398, 198089, -129229, -546313, 493402, -429792, -290510, -253252, -293591, 235755, -372590, 126760, 491670,
        363788, 281735, 527688, -262211, -387086, 218518, 372942, 430089, -85166, -136439, -442631, 444942, 222378, -382502, 483845, 211997, -160464, 539794, 299625, 21495, 303000, 50598, 363647,
        -169734, 507160, -239002, 38905, -380255, -421730, 398512, 497697, -195994, -359741, 200484, 120892, 244454, -584256, -273069, -163032, -478946, -441271, -382870, -154119, -275001, 22798,
        245623, -399550, 287023, 76378, -169737, 546609, 220057, -307094, -364841, 499324, -159330, -568679, 465161, -221706, 579306, 79993, 138311, -419992, 486358, -81176, -16117, 258250, -419364,
        -231481, 227683, -207085, 351215, 580870, -293665, -555527, 141857, 189480, -68788, -546102, -14871, -554917, 447765, -478627, 78241, -174224, 326800, 573073, -26316, -61998, -418186, 59570,
        322281, -18540, 543431, -490520, -211079, -593702, -168196, 280596, -365957, 380525, 86350, -398705, -80021, -68042, -455482, -326453, 161828, 441446, -513844, 305710, 347467, -484546,
        -451888, 433152, 505827, 442371, -111490, 474818, 129197, 232666, 493296, -566406, -273795, -334127, 594412, -405121, 589993, -559967, 196306, 17649, 114052, -192167, 118413, -520174, 9095,
        72997, -72327, 192948, -337742, -171602, -97266, -464709, -160740, 140213, -299483, 522012, 307883, 399166, 229470, -406582, -168788, 591476, -232937, -306744, 416391, -194439, 241535, 360093,
        154576, 269829, 156728, -241586, -163873, -84086, 168965, 136489, 257752, 351340, 51964, -317544, 29576, -273908, -452286, 428847, -333711, -558388, -215598, 104658, 324973, -121800, -518718,
        -238016, 475075, -140504, 357590, 119459, 84831, 133621, -197236, -217846, -181933, -483140, 58375, 383558, 232105, -175795, -580121, -501145, 129886, 271616, -103045, -339857, 47161, -557374,
        -401535, -535796, 248529, -188638, 91766, 456064, -87809, -403877, 156909, -276961, 460881, 89217, 154442, -76425, 32038, -381836, -335586, 326399, -362485, -357178, -537569, -275730, -570632,
        -589394, -97176, 418366, 503319, 167716, -214835, 519746, 595712, -414845, 384612, -114654, -95411, 150576, 144676, -377374, 472251, 63285, 154117, -84932, 334399, 413746, -47127, -22361,
        -553407, -526034, 9624, 36756, 388852, -452388, 106364, 439729, 579180, 492276, 34799, 334241, -114782, 381049, -450353, 335365, -131514, 556661, -362147, -386226, 418799, -144668, -275345,
        115318, 134563, -42432, 18623, -211442, -518693, -126957, -352327, -573198, 593733, -377303, 403255, -491208, 453333, 514995, 250277, -576142, 464818, -343631, -362597, 260797, -318935, 61494,
        226302, -554440, 136885, -402182, -462896, 139167, -265132, -67914, -336666, -534159, -490950, -337600, -95504, 207026, -91921, 74887, 5457, -381568, -99837, -497088, -293348, 4609, 281644,
        -308310, 55378, 317985, 174232, -49098, 574370, 357005, -227748, 201844, 81284, 471257, 188629, -348594, -294110, 42526, 75635, -29806, -108748, -477927, -190381, 206736, -89130, 144579, 7742,
        445984, -51715, 582270, 65443, -474534, -450300, -584597, 11965, -443980, 122479, 197067, 171684, -94662, 409242, -204539, 117235, -35341, -238544, -495931, 479765, 573233, 482142, 237933,
        -396344, 539422, 439392, -65002, 553778, -483116, 381807, 142362, 437692, -214768, -118291, -64387, -388124, 238859, 34644, -312891, 584207, 57772, -61654, 152487, -426099, -471821, -40319,
        -79806, 463536, 512696, 177623, -69736, -84054, -473591, 317920, -426926, -495351, 465778, -241357, -289633, 441161, 362187, 102256, 102931, -397589, -114568, 266556, 558474, 164613, -219023,
        45935, 5949, -57197, -535702, 99969, -34121, -568937, -31773, -556003, -417630, 247361, -437020, -476065, 590294, 349583, -360608, 448647, 455933, 282533, 426527, -515754, 223269, 513916,
        361165, -525785, -192643, 426738, -69872, -360710, 376086, -111926, -288619, -49688, -145979, -414745, -345609, 311806, 203814, -271386, -421091, 147989, -440359, -460888, 445283, -368640,
        -785, 368093, 68593, -457706, 489169, 172661, 402639, -39431, 517806, 587950, -21729, -128341, -190247, -65219, 304435, -8825, 412081, 367536, -311987, 514562, -205558, -88492, -405252,
        453706, -381828, -372600, 205494, -78442, 309605, 437175, -288136, 382223, 331811, 137563, 89594, -285988, 484839, 281643, 139912, -229210, 427092, 462609, 29199, 415077, -354605, 334262,
        323173, 101503, -26818, 589797, -503679, 579203, -216247, -7106, -491896, 81178, -265686, -542459, 448992, -356918, -329080, 443805, 366790, -8796, -67815, 200563, 508616, -355835, -103225,
        -245608, -444158, -477996, -112667, -556085, -345180, 377394, 103958, 31900, -167947, -482655, -115708, 64493, 588276, -341187, 7056, -487301, -64097, 336443, 293385, -546621, 393138, -15841,
        -158431, -481584, 403378, 488511, -279278, 189639, 80424, 335452, -265522, -306252, 373120, -534559, -386224, -69912, 724, -123838, -282688, 520230, -529204, 488479, -398197, 192476, -9829,
        329387, 67180, 188864, 277775, -158610, -570005, -132065, 435511, 446656, -245811, -530643, 365696, 205509, -197716, 293128, -326248, -178340, -121648, -57220, 155213, 522129]
s = "RRLRLRRLRRLRLLRLRLLRRLLLLRLRLRLLLRLLLLRRLLLLRRRLRLRRLRLRRRLRLRRLLLLLLLLRLRRRLRRRLRRLLRRRLRLRLLRRLRLRLLLLLLRRLLRRLRLLRLRRLLLLLRRLRLRRLRRRLLLRRLRRLRLRLRRRRRLRLRLRLRLRRRLRLRLRLRLRLLLRLLLLRRLRRRRLRRRLRRLRLLRRRLLLLRRLLRLRLLRLLRRRRRRRLLRRLRLLLRLRRLRLLRLRLRLLLLRRLLLRRRRRRRLRRRRRLRLLLRRRRLRLLLRLRRRLRLRLLRRRRRRLLRRRRRRRRRLRRRLLRLRRLRRRLLLLRLRRLRRLLRRRRLLRRLRLLRLRRLLRRLRRRLRRLLLLLRRRLRLRLLRLLLLRRLRRRLLLLRLRRLLRLRLLLRRRRLRRRLRRLLRRLLLRLRRLRLLLLLRLLRRRLLRRRRRRRRLLRLLRLLLRRRRRLLRLLRRRRLRRRRLRRLLLRLRRRLLLLLLRRLRLLLLRRLLRRRLLLLLLLLRLLRRRLRLLRLLLRRRLLLLLLLRLRLRLRRLLLRLLLRLLLRLRLLRLLRLLRRRRRRRLRLLLLRRRLLRRLRRRRLLLRRRLLRLRRLRLRLLRRLLLRLRLLRLLLLRLLRRRRRLLRLLLRLRLLLLLRLLLLRLLRLRRRRLLLRLRRRRRRRRRLRLLRLRRLLRRLRRRRLLLLLRRLRRLRRRLRRLRRRRLLLRLRLLLLLRLLRRLRLLLLRLLRLLRRRRRLRRLRLLLRLRRRLRL"
d = 2
print(A.sumDistance(nums, s, d))
