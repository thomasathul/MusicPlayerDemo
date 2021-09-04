# TEST PLAN:-

## High level test plan

| **Test ID** | **Description**                                     | **Exp O/P** | **Actual O/P** | **Type Of Test** |
| ----------- | --------------------------------------------------- |  ----------- | -------------- | ---------------- |
| HR01        | To test if the choices given in menu screen are working properly    | SUCCESS     | SUCCESS        | Technical       |
| HR02        | To test if the song could be heard                    | SUCCESS     | SUCCESS        | Scenario        |
| HR03        | To test if the song list retrieved is correct                                  | SUCCESS     | SUCCESS        | Technical        |
| HR04        | To test if the program allows the user to login/signup                                   | SUCCESS     | SUCCESS        | Scenario        |
| HR05        | To test if the data is stored in database                                   | SUCCESS     | SUCCESS        | Scenario        |

## Low level test plan

| **Test ID** | **Description**                                                                         | **Exp I/P**                                                                  | **Exp O/P**      | **Actual O/P**   | **Type Of Test** |
| ----------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------- | ---------------- | ---------------- |
| LR01        | To test if the username provided for signup is valid                  |     Username                             | True          | True         | Technical        |
| LR02        | To test if the username provided for signup is invalid                                         | Username                          | False          | False         | Technical        |
| LR03        | To test if the password provided for signup is valid                                              | Password | true          | True         | Technical        |
| LR04        | To test if the password provided for signup is invalid              | Password | False      | False       | Technical        |
| LR05        | To test if the program returns the correct hashed value                                 | Password                                                 |   469        |   469       | Technical        |
| LR06        | To test if the data is saved in database           | Username, Password                                                  | True       | True      | Scenario       |
| LR07        | To test if the program accurately searches the account from database                                 | Username,Password                                                  | True          | True          | Technical        |
| LR08        | To test if the program accurately searches the account from database                                     | None,None                                                  | False       | False      | Technical        |
| LR09        | To test if the program successfully searched the keyword result                            | trackname                                                 | ([music_list],[track_list])          | ([music_list],[track_list])        | Technical        |
| LR10        | To test if the program returns music list from database                                      |                                                   |  ([music_list],[track_list])       | ([music_list],[track_list])      | Technical        |
| LR09        | To test if the program selects the valid trackname from database                                              | trackname                                                                   | "Zaalima"          | "Zaalima.wav"          | Technical        |
| LR10        | To test if the program encounters invalid trackname                          | trackname                                                                  | "XYZsong" | "XYZsong" | Technical        |
| LR11        | To test if the username exists in database                        | Username                                                                  | True       | True       | Technical        |
| LR12        | To test if the username doesn't exist in database                        | Username                                                                  | False       | False       | Technical        |
| LR13        | To test if the song is played                        |                                                                  | True       | True       | Scenario        |


