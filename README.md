# DevOps_Oct2021_Team-5

Project Team
</br>Scrum master: Megan Png
</br>QA: Huan Hui Ying
</br>Tech Lead: Claris Toh
</br>Developers: Amanda Chan


  <h2>Latest Changes</h2>
  
  <h2>Links</h2>
  <a href="https://docs.google.com/spreadsheets/d/1tX3el3ndlgzSFnqHNxrp61wxTIDeNvBg638vxIcpcmc/edit?usp=sharing">Link to Project Schedule</a> </br>
  <a href="https://docs.google.com/document/d/1wb-C8OHoWW_vbBH2aLk3durw-UetdH7pjSJJaAELosY/edit?usp=sharing">Link to Development Tech Notes</a> </br>
  <a href="https://docs.google.com/document/d/18b-z5AkiJ0Z17K83W6AaTdXhWpSoJKHzDPN01gHf85Q/edit?usp=sharing">Link to User Acceptance Criteria</a> </br>
  
  <h2>Sprint Retrospectives</h2>
  <a href="https://docs.google.com/document/d/1HH2GRwInOwWczK_qj-3854chnIlAdsrY/edit?usp=sharing&ouid=112796443500104222435&rtpof=true&sd=true">Link to Sprint 1 Retrospective</a> </br>
  <a href="https://docs.google.com/document/d/1yt4ywSWMIp6nAhfCosxCW-nYPpaOqdlr/edit?usp=sharing&ouid=112796443500104222435&rtpof=true&sd=true">Link to Sprint 2 Retrospective</a> </br>

  <h2>Project Background</h2>


  <h2>Team's Approach</h2>


  <h2>Different Requirements of the Assignment</h2>
  <ol>
  <li>Display Main Menu</li>
  1.1 Start New Game</br>
  1.2 Load Saved Game</br>
  1.3 Exit Game </p>
  </br>
  
  <li>Playing the Game</li>
  2.1 Building a Building </br>
  2.2 See Remaining Buildings </br>
  2.3 See Current Score </br>
  2.4 Save Game </br>
  2.5 Exit to Main Menu </br>
  </br>
  
  <li>End of Game</li>
  3.1 Exit Game
  </ol>
  
<h2>SDLC Model to Consider</h2>
<ol>
  <li> V-Shape Model </br>
    </br>
    <strong><u>Definition of V-Shaped Model: </u></strong> </br>
    <p>The V-Shaped Model is a software development life cycle that is linear in a V-Shape and has a structured method in producing a software product. Its process includes verification followed by implementation and followed by validation, and the verification design is validated by a corresponding test. Verification is the procedure of reviewing and analysing requirements and it is usually carried out through small sections of codes or documentations. Validation is the testing of code using nonfunctional and functional test requirements and usually is in the format of steps and the clients’ or end-users’ acceptance. For every step of the development cycle, there is a testing stage that is directly connected to it, and the next step of the development cycle is only started after the previous step is completed. (Tutorials Point, 2021)

As it is often costly to return back to a previous stage of the lifecycle and modify it, there must be very defined and distinct requirements before the project begins. It would suit projects where the requirements are distinct, well documented and unchangeable, where the definition of the product is secure, where the project timeline is short, where the technology used is not dynamic and the project team has knowledge on how to use it.  (Tutorials Point, 2021)
</p>
</br>
    <strong><u>Pros: </u></strong> </br>
    <ul>
      <li>Easy to understand and use
      <li>Simple to oversee due to:
        <ul>
          <li>V-Shaped Model method being uncomplicated
          <li>Inflexibility of model
        </ul> 
      <li>Each stage has distinct goals and a review procedure.
      <li>Good for smaller, simple projects where requirements are defined and comprehensible   (Tutorials Point, 2021)
      <li>Higher possibility of success compared to Waterfall Model
        <ul>
          <li>Due testing activities such as test designing being carried out before coding resulting in saved time.
        </ul>
       <li>Defects can be discovered in early phases of project due to validation for each stage having to be carried out before progressing to the next
       <li>Prevents defects from brought from one stage to another and possibly advancing in severity (Try QA, 2013)
    </ul>
    </br>
    <strong><u>Cons: </u></strong> </br>
    <ul>
      <li>Not suitable for complicated and object oriented projects
      <li>Not suitable for lengthy and evolving projects 
      <li>Does not allow for change easily
      <li>Not appropriate for projects where there is average to high chance of requirements being modified
      <li>Hard to return and modify a feature or functionality once application has reached the phase of testing
      <li>Working software is only built in the late stages of development. (Tutorials Point, 2021)
        <ul>
          <li>No prototypes created in early stages of development
        </ul>
       <li>If modifications are made during developments, both requirements and tests need to be updated, causing delays. (Try QA, 2013)
    </ul>
    </br>
    <strong><u>Suitability of V-Shaped Model: </u></strong> </br>
    <p>Although there may be some benefits in using this V-Shape Model method, such as that it is easy to use and understand, lessening the time needed to learn how to use it, it is still not suitable for this project. There is a high possibility for change or addition in the requirements later in the development of the project, and as the V-Shaped Model method does not allow for changes easily and is not suitable for projects with average to high possibility of their requirements being modified, it is not appropriate to be used for this project.

If this SDLC was used, whenever the requirements were changed, the whole development cycle would have to restart as they would need to return back to the requirements stage. This would cause delays in the project timeline as it is only possible to move on to the next stage after the previous stage is completed, harming the project negatively as there is a fixed deadline. Tests would also need to be updated to adjust to the modified requirements, resulting in further delays as well. Working software is also only produced in the later stages of development, which would result in less time to fix any crashes, to review the user experience and make changes to the software to improve it, like discovering the need for validation at areas of the project and adding it, or to make other changes to the software. Therefore, the V-Shaped Model is not suitable to be used as the chosen SDLC for this project.
</p>
  <li> Incremental Model + Iterative Model (Evoultionary) </br>
    </br>
    <strong><u>Definition of Evolutionary model: </u></strong> </br>
    <p>In the Incremental model, requirements are broken down into numerous standalone modules. After each increment, more functions are added on from the previous. For each      increment, it consists of 4 phases consisting of Requirement Analysis, Design and Development, Testing and Implementation. Requirement Analysis is a key step to better understand and plan how the requirements will be broken down. (javaTpoint, Incremental Model, n.d.)
In the Iterative model, requirements are broken down into numerous cycles of development. This would mean multiple builds with the same requirement. It is a subset of the Incremental model. Each build consists of 3 phases, Requirements, Design and Implement. This model is great to use when the software development is huge and the requirements are comprehensible and defined clearly. (javaTpoint, n.d.)
The Evolutionary model combines both the Incremental model and Iterative model. After each increment, the deliverables will be presented to the client to test. The advantage of this is that it increases the client’s confidence since they are able to verify the product and developers are able to get their feedback straight away as well. Hence, this model allows for change in requirements which may stray from the original product initially planned. This model is great when clients want to start using the core functions of the products first rather than waiting for the fully developed software. (pp_pankaj, 2019)
</p>
    </br>
    <strong><u>Pros: </u></strong> </br>
    <ul>
      <li>Able to gather feedback from client as they test the features after each increment
      <li>Lesser margin of error since it is being tested in depth
      <li>Fitted for object-oriented development
      <li>Changes can be made during development after each iteration
(easytechnotes, 2021)
    </ul>
    </br>
    <strong><u>Cons: </u></strong> </br>
    <ul>
      <li>It may be difficult to divide the deliverables into several increments and deliver what is required
      <li>Unsuitable for smaller scale projects
      <li>Fitted for object-oriented development
      <li>Can be costly (easytechnotes, 2021)
    </ul>
    </br>
    <strong><u>Suitability of Evolutionary model: </u></strong> </br>
    <p>There are some benefits of using the Evolutionary model in this project in that it is fitted to be used in object-oriented development and the model is fitted to manage any changes made to the requirements. However, the project on hand is a smaller project and it will be difficult to break down the deliverables into different increments for the client to test. In addition, changes made to requirements can be made after each increment and not during the phase. Hence, the Evolutionary model is not the best fitted choice in this project.
</p>
  <li> Agile 
  <li> Spiral </br>
  </br>
    <strong><u>Definition of Spiral Model: </u></strong> </br>
    <p>The Spiral model is a system development life cycle (SDLC) used mainly for large-scale, high-risk projects. It combines the waterfall model and iterative model to allow frequent releases.
It consists of 4 main phases which are cycled until the project’s completion.
<ul>
  <li>Requirement Gathering
    <p>This stage is where the requirements of the project are collected. In subsequent spirals in the course of the project, any other system requirements are also realised in this phase. </p>
    <li>Analysis
      <p>Using the requirements gathered in the previous phase, analysis will take place to consider different solutions that could satisfy the requirements. During this phase, risk analysis will take place to identify and estimate the technical feasibility such as schedule slippage and cost-overrun (What is Spiral Model? Definition of Spiral Model, Spiral Model Meaning - The Economic Times, 2021). </p>
     <li>Development and Testing
       <p>After doing the analysis and choosing the best solution, development will take place. The product that is roughly done up in the first few spirals will be considered as a Proof of Concept to get the users’ feedback in the next stage. In subsequent spirals, when the requirements get clearer, the working build will be sent with version numbers to the users to get their feedback (What is Spiral Model? Definition of Spiral Model, Spiral Model Meaning - The Economic Times, 2021). </p>
      <li>Evaluation and Review
        <p>At the end of the first spiral, the users will evaluate the product and provide their feedback. Their feedback will carry into the next iteration as new requirements.
  </br>
Due to the nature of the Spiral Model, this model requires heavy documentation to monitor and keep track of risks, constraints, additional requirements, progress as well as feedback from users. </br>
  </br>
However, the constant iterations will allow for changes in requirements easily. </br>
</p>
    </br>
    <strong><u>Pros: </u></strong> </br>
    <ul>
      <li>Very flexible
      <li>Suitable for large scale projects
      <li>Easy to monitor
      <li>Accommodates for change in requirements easily
      <li>Allows additional post-project functionality
      <li>Good for projects of high-risk (Spiral Model: When to Use? Advantages & Disadvantages, 2021)
      <li>Suitable for budget heavy projects 
    </ul>
    </br>
    <strong><u>Cons: </u></strong> </br>
    <ul>
      <li>Heavy on documentation
      <li>Rules and SOP to be followed closely 
    </ul>
    </br>
    <strong><u>Suitability of Evolutionary model: </u></strong> </br>
    <p>Looking at the pros and cons of the Spiral Model, as well as the project case study, this project will not fully make use of the features in this SDLC. </br>

This model is flexible and allows changes and or additions to requirements, which aligns with the project case study where it states that additional requirements might be added. </br>

This model also values heavy documentation, which might not be necessary for this project. </br>

The Spiral model allows risk assessment in the Analysis stage in each iteration. With constant risk assessment, a high risk project that has a high budget would benefit from this. This project is not considered high risk and does not have a budget to work with, hence this model might not be suitable. </br>

This model is also time consuming, since multiple iterations must be completed. The speed of each iteration would depend on the team’s ability to deliver functions on time. The team has projects to work on other than this one, so they might not be able to fully commit themselves to this project. </br>

Finally, the model doesn’t encourage back tracking in stages, so if the project were to strictly follow the spiral model, it might pose an inconvenience. </br>

Therefore, the Spiral Model is not suitable for this project and another SDLC should be considered. </br>

</p>
  <li> Big Bang
  <li> References </br>
    <ul>
      <li>Try QA. (2013). What are V-model- advantages, disadvantages and when to use it? Retrieved from Try QA: http://tryqa.com/what-is-v-model-advantages-disadvantages-and-when-to-use-it/
      <li>Tutorials Point. (2021). SDLC - V-Model. Retrieved from Simple Easy Learning: https://www.tutorialspoint.com/sdlc/sdlc_v_model.htm
      <li>easytechnotes. (2021, June 06). Evolutionary Model Advantages and Disadvantages. Retrieved from easytechnotes: https://easytechnotes.com/evolutionary-model/
      <li>ICT. (2021/2022). DevOps (DOP) Lecture 1-1. Retrieved from Emerging Trends in Infocomm Technology (ETI): https://learn-ap-southeast-1-prod-fleet03-xythos.content.blackboardcdn.com/5dfa8616972ac/13028682?X-Blackboard-Expiration=1636016400000&X-Blackboard-Signature=mI6rkrRvvw8cGvRvlhCqGJUnupHuNwyqqzGlsJEpoRc%3D&X-Blackboard-Client-Id=180274&response-cache-cont
      <li>What is Spiral Model? Definition of Spiral Model, Spiral Model Meaning - The Economic Times. (2021). Spiral Model. The Economic Times. https://economictimes.indiatimes.com/definition/spiral-model
      <li>javaTpoint. (n.d.). Incremental Model. Retrieved from javaTpoint: https://www.javatpoint.com/software-engineering-incremental-model 
      <li>javaTpoint. (n.d.). Iterative Model. Retrieved from javaTpoint: https://www.javatpoint.com/software-engineering-iterative-model 
      <li>pp_pankaj. (2019, April 30). Software Engineering | Evolutionary Model. Retrieved from GeeksforGeeks: https://www.geeksforgeeks.org/software-engineering-evolutionary-model/ 
        
</ol>
